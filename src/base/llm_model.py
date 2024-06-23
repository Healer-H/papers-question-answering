import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

API_KEY = "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"

def get_llm(model_name="llama3-70b-8192", temperature=0.2):
    return ChatGroq(
        temperature=temperature,
        model=model_name,
        api_key=API_KEY
    )
    
