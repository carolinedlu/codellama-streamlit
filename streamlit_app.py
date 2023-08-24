from transformers import AutoTokenizer, AutoModelForCausalLM
import streamlit as st

@st.cache_data
def load_model():
  tokenizer = AutoTokenizer.from_pretrained("TheBloke/CodeLlama-13B-Python-fp16")
  model = AutoModelForCausalLM.from_pretrained("TheBloke/CodeLlama-13B-Python-fp16")
  return tokenizer, model
  
tokenizer, model = load_model()

prompt = st.text_input("your prompt)
