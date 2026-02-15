from dotenv import load_dotenv
from langchain_ollama import OllamaEmbeddings
from model import get_ollama_model

load_dotenv()

# embedd text
embeddings = OllamaEmbeddings(model=get_ollama_model())
text = "this is some normal text string which we want to embed"
embed_text = embeddings.embed_query(text)
print(embed_text)

# embedd csv file
from langchain_community.document_loaders import CSVLoader
loader = CSVLoader("static_data/test.csv")
documents = loader.load()
# rememer files are not embedded, only text is embedded, so we need to extract the text from the documents
embed_docs = embeddings.embed_documents([doc.page_content for doc in documents])
print(len(embed_docs))

