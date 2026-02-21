from langchain_chroma import Chroma
from langchain_community.document_loaders import WikipediaLoader
from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv
from langchain_text_splitters import CharacterTextSplitter
from model import get_ollama_model, get_groq_model
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


# loader = WikipediaLoader(query="MKUltra")
# documents = loader.load()
# text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=500)
# docs = text_splitter.split_documents(documents)

# print(len(docs))

embedding_function = OllamaEmbeddings(model=get_ollama_model())
# db = Chroma.from_documents(docs, embedding_function, persist_directory="./some_new_mkultra")

db_connection = Chroma(persist_directory="./some_new_mkultra", embedding_function=embedding_function)
retriever = db_connection.as_retriever()


## METHOD 1: retrieve documents -> compress using LLM -> return compressed docs
# retrieve documents
# docs = retriever.invoke("When was this declassified?")

# # now manually compress the retrieved documents using LLM
# llm = get_groq_model()
# compressed_docs = []

# for i,doc in enumerate(docs):
#     response = llm.invoke(
#         f"Extract only the parts relevant to the question:\n"
#         f"Question: When was this declassified?\n\n"
#         f"Document:\n{doc.page_content}"
#     )
#     compressed_docs.append(response.content)

# print("Compressed Documents:", compressed_docs)


## METHOD 2: RETRIEVAL CHAIN
llm = get_groq_model()
rag_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough(),
    }
    | ChatPromptTemplate.from_template("""
        Answer the question using only the context below.

        Context:
        {context}

        Question:
        {question}
    """)
    | llm
    | StrOutputParser()
)

response = rag_chain.invoke("When was this declassified?")
print(response)