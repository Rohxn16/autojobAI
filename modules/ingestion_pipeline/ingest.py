import shutil
import os
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

def ingest_string_to_vector_database_with_chunking(text: str):

    """
    Apply chunking and embedding to text and upload it to vector database

    :param text: text to ingest
    :return: None
    """

    embeddings = OllamaEmbeddings(
        model='nomic-embed-text:latest'
    )

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        separators=['\n','\n\n', ' ', '']
    )

    chunks = text_splitter.split_text(text)

    vector_db = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory="./my_vector_db"  # Optional: saves to disk
    )

def clear_previous_session(persist_directory: str = "./my_vector_db"):

    """
    Clear the vector database from the previous session

    :return: None
    """
    if os.path.exists(persist_directory):
        shutil.rmtree(persist_directory)
        print('Previous session cleared. Proceeding...')
    else:
        print('No existing Session to clear. Proceeding.....')