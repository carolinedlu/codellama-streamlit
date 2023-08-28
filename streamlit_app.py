import streamlit as st
import replicate
import os

st.set_page_config(page_title="🦙💬 Code Llama Chatbot")
os.environ['REPLICATE_API_TOKEN'] = st.secrets["REPLICATE_API_TOKEN"]
         
if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a programming-related question!"}
    ]

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

def generate_codellama_response(prompt_input):
    # string_dialogue = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
    # for dict_message in st.session_state.messages:
    #     if dict_message["role"] == "user":
    #         string_dialogue += "User: " + dict_message["content"] + "\n\n"
    #     else:
    #         string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    # output = replicate.run('replicate/codellama-13b:1c914d844307b0588599b8393480a3ba917b660c7e9dfae681542b5325f228db', 
    #                        input={"prompt": f"{prompt_input}",
    #                               "temperature":0.1, "top_p":0.9, "max_length":512, "repetition_penalty":1})
      output = replicate.run('replicate/codellama-13b:1c914d844307b0588599b8393480a3ba917b660c7e9dfae681542b5325f228db', 
                           input={"prompt": f"{prompt_input}",
                           "temperature":0.1, "top_p":0.9, "max_length":512, "repetition_penalty":1})
    
      return output

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
          response_codellama = generate_codellama_response(prompt)
          response = ""
          resp_container = st.empty()
          for delta in response_codellama:
            response += delta
            # resp_container.markdown(response)
            resp_container.write(response)
          message = {"role": "assistant", "content": response}
          st.session_state.messages.append(message) # Add response to message history

# Replicate Credentials
# with st.sidebar:
#     st.title('🦙💬 Code Llama Chatbot')
#     # if 'REPLICATE_API_TOKEN' in st.secrets:
#     #     st.success('API key already provided!', icon='✅')
#     #     replicate_api = st.secrets['REPLICATE_API_TOKEN']
#     # else:
#     #     replicate_api = st.text_input('Enter Replicate API token:', type='password')
#     #     if not (replicate_api.startswith('r8_') and len(replicate_api)==40):
#     #         st.warning('Please enter your credentials!', icon='⚠️')
#     #     else:
#     #         st.success('Proceed to entering your prompt message!', icon='👉')
#     st.markdown('📖 Learn how to build this app in this [blog](https://blog.streamlit.io/how-to-build-a-llama-2-chatbot/)!')
# os.environ['REPLICATE_API_TOKEN'] = replicate_api

# # Store LLM generated responses
# if "messages" not in st.session_state.keys():
#     st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# # Display or clear chat messages
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.write(message["content"])

# def clear_chat_history():
#     st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
# st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Function for generating LLaMA2 response
# Refactored from https://github.com/a16z-infra/llama2-chatbot
# def generate_llama2_response(prompt_input):
#     string_dialogue = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
#     for dict_message in st.session_state.messages:
#         if dict_message["role"] == "user":
#             string_dialogue += "User: " + dict_message["content"] + "\n\n"
#         else:
#             string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
#     output = replicate.run('replicate/codellama-13b:1c914d844307b0588599b8393480a3ba917b660c7e9dfae681542b5325f228db', 
#                            input={"prompt": f"{string_dialogue} {prompt_input} Assistant: ",
#                                   "temperature":0.1, "top_p":0.9, "max_length":512, "repetition_penalty":1})
#     return output

# # User-provided prompt
# if prompt := st.chat_input(disabled=not replicate_api):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.write(prompt)

# # Generate a new response if last message is not from assistant
# if st.session_state.messages[-1]["role"] != "assistant":
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             response = generate_llama2_response(prompt)
#             placeholder = st.empty()
#             full_response = ''
#             for item in response:
#                 full_response += item
#                 placeholder.markdown(full_response)
#             placeholder.markdown(full_response)
#     message = {"role": "assistant", "content": full_response}
#     st.session_state.messages.append(message)
