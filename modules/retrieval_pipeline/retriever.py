from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

embeddings = OllamaEmbeddings(model="nomic-embed-text")

def retrieve_top_k(query: str, k: int = 3):
    """
    Performs similarity search and returns the top k chunks.
    :param query: query to search for
    :param k: number of chunks to return

    :return: list of top k chunks
    """
    vector_db = Chroma(
        persist_directory="./my_vector_db",
        embedding_function=embeddings
    )
    
    # Use 'similarity_search' to get Document objects
    # Or 'similarity_search_with_score' to see the distance/similarity values
    results = vector_db.similarity_search(
        query,
        k=k
    )

    return results