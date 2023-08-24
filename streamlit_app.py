from transformers import AutoTokenizer, AutoModelForCausalLM
import streamlit as st
from transformers import pipeline

# @st.cache_data
# def load_model():
pipe = pipeline("question-answering", model="TheBloke/CodeLlama-13B-Python-fp16")
# tokenizer = AutoTokenizer.from_pretrained("TheBloke/CodeLlama-13B-Python-fp16")
# model = AutoModelForCausalLM.from_pretrained("TheBloke/CodeLlama-13B-Python-fp16", ignore_mismatched_sizes=True)
# return tokenizer, model
response = pipe(["Write a Python program to sum two integers"])
st.write(response)
  
# tokenizer, model = load_model()

# prompt = st.text_input("your prompt")
# access_token = "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"
# model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", load_in_4bit=True,  use_auth_token=access_token)
# tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True, use_auth_token=access_token)

# model_inputs = tokenizer(prompt, return_tensors="pt").to("cuda:0")
# output = model.generate(**model_inputs)
# st.write(tokenizer.decode(output[0], skip_special_tokens=True))
