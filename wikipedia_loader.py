from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

chat = ChatGroq(model=os.getenv("GROQ_MODEL_NAME"), temperature=0,api_key=os.getenv("GROQ_API_KEY"))
response = chat.invoke("Hello world!")
print(response)