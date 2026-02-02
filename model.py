from langchain_groq import ChatGroq
import os

def get_model():
    return ChatGroq(model=os.getenv("GROQ_MODEL_NAME"), temperature=0,api_key=os.getenv("GROQ_API_KEY"))