# reading from file and getting data
from langchain_community.document_loaders import CSVLoader, BSHTMLLoader
loader = BSHTMLLoader("static_data/test.html")
documents = loader.load()
print(documents[0])