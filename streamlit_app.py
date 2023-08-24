from transformers import AutoTokenizer, AutoModelForCausalLM
import streamlit as st

tokenizer = AutoTokenizer.from_pretrained("TheBloke/CodeLlama-13B-Python-fp16")
model = AutoModelForCausalLM.from_pretrained("TheBloke/CodeLlama-13B-Python-fp16")
