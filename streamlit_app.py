from transformers import AutoTokenizer, AutoModelForCausalLM
import streamlit as st

@st.cache_data
def load_model():
  tokenizer = AutoTokenizer.from_pretrained("TheBloke/CodeLlama-13B-Python-fp16")
  model = AutoModelForCausalLM.from_pretrained("TheBloke/CodeLlama-13B-Python-fp16")
  return tokenizer, model
  
tokenizer, model = load_model()

prompt = st.text_input("your prompt")
# access_token = "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"
# model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", load_in_4bit=True,  use_auth_token=access_token)
# tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True, use_auth_token=access_token)

model_inputs = tokenizer(prompt, return_tensors="pt").to("cuda:0")
output = model.generate(**model_inputs)
st.write(tokenizer.decode(output[0], skip_special_tokens=True))
