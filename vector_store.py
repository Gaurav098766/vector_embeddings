import chromadb
from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv
from langchain_text_splitters import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader

from model import get_ollama_model

load_dotenv()

# load dcouements-> split chunks 
# split chunks -> emedding -> emed chunks 
# -> vectors ->vector chunks 
# -> save chroma db -> query -> similarity search -> return results

loader = TextLoader("static_data/fdr_state_of_union_1941.txt",encoding="utf-8")
documents = loader.load()
text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=200)
docs = text_splitter.split_documents(documents)
print(docs)

embedding_function = OllamaEmbeddings(model=get_ollama_model())
db = Chroma.from_documents(docs, embedding_function, persist_directory="./speech_new_db")

db_new_connection = Chroma(persist_directory="./speech_new_db", embedding_function=embedding_function)

new_doc = "What are the four essential human freedoms Roosevelt described for the future world?"

similar_docs = db_new_connection.similarity_search(new_doc, k=1)
# print(similar_docs[0].page_content)
