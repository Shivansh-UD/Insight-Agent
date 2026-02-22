import chromadb
from sentence_transformers import SentenceTransformer

'''
What This Does: 

    1. Converts text → vector embeddings

    2. Stores them

    3. Retrieves similar text when queried

This is memory layer.
'''

# Initialize embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize Chroma client
client = chromadb.Client()

# Create or get collection
collection = client.get_or_create_collection(name="research_memory")


def add_documents(documents):
    """
    documents: list of strings
    """

    embeddings = embedding_model.encode(documents).tolist()

    ids = [f"id_{i}" for i in range(len(documents))]

    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=ids
    )


def retrieve(query, top_k=3):

    query_embedding = embedding_model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    return results["documents"][0]