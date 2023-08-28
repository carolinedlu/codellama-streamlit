# from transformers import AutoTokenizer, AutoModelForCausalLM
# import streamlit as st
# from transformers import pipeline

# # @st.cache_data
# # def load_model():
# pipe = pipeline("question-answering", model="TheBloke/CodeLlama-13B-Python-fp16")
# # tokenizer = AutoTokenizer.from_pretrained("TheBloke/CodeLlama-13B-Python-fp16")
# # model = AutoModelForCausalLM.from_pretrained("TheBloke/CodeLlama-13B-Python-fp16", ignore_mismatched_sizes=True)
# # return tokenizer, model
# response = pipe(["Write a Python program to sum two integers"])
# st.write(response)
  
# # tokenizer, model = load_model()

# # prompt = st.text_input("your prompt")
# # access_token = "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"
# # model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", load_in_4bit=True,  use_auth_token=access_token)
# # tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True, use_auth_token=access_token)

# # model_inputs = tokenizer(prompt, return_tensors="pt").to("cuda:0")
# # output = model.generate(**model_inputs)
# # st.write(tokenizer.decode(output[0], skip_special_tokens=True))


import streamlit as st
import replicate
import os

os.environ['REPLICATE_API_TOKEN'] = st.secrets["REPLICATE_API_TOKEN"]

# st.set_page_config(page_title="Chat with the Streamlit docs, powered by LlamaIndex", page_icon="🦙", layout="centered", initial_sidebar_state="auto", menu_items=None)
# openai.api_key = st.secrets.openai_key
# st.title("Chat with the Streamlit docs, powered by LlamaIndex 💬🦙")
# st.info("Check out the full tutorial to build this app in our [blog post](https://blog.streamlit.io/build-a-chatbot-with-custom-data-sources-powered-by-llamaindex/)", icon="📃")
         
if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question about Streamlit's open-source Python library!"}
    ]

# @st.cache_resource(show_spinner=False)
# def load_data():
#     with st.spinner(text="Loading and indexing the Streamlit docs – hang tight! This should take 1-2 minutes."):
#         reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
#         docs = reader.load_data()
#         service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert on the Streamlit Python library and your job is to answer technical questions. Assume that all questions are related to the Streamlit Python library. Keep your answers technical and based on facts – do not hallucinate features."))
#         index = VectorStoreIndex.from_documents(docs, service_context=service_context)
#         return index

# index = load_data()
# chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True, system_prompt="You are an expert on the Streamlit Python library and your job is to answer technical questions. Assume that all questions are related to the Streamlit Python library. Keep your answers technical and based on facts – do not hallucinate features.")
# chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

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
                           input={"prompt": f"{prompt_input}",})
      return output

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
          response_codellama = generate_codellama_response(prompt)
          response = ""
          resp_container = st.empty()
          for delta in response_codellama
            response += delta
            #delta.choices[0].delta.get("content", "")
            resp_container.markdown(response)

            # response = generate_codellama_response(prompt)
            # response_text = " "
            # for it in response:
            #   # st.write(it)
            #   response_text += it
            # st.write(response_text)
            # # st.write(response)
            # # st.write(response.gi_code)
            # # st.write(type(response))
            # message = {"role": "assistant", "content": response}
            # st.session_state.messages.append(message) # Add response to message history


# # App title
# st.set_page_config(page_title="🦙💬 Code Llama Chatbot")

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
