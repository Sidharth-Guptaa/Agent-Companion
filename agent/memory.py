from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.memory import VectorStoreRetrieverMemory
import os

def get_memory():
    embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])
    store = Chroma(embedding_function=embeddings, persist_directory="./chroma_db")
    return VectorStoreRetrieverMemory(retriever=store.as_retriever())
