import chromadb

# Persistent database
client = chromadb.PersistentClient(
    path="database/chroma"
)

collection = client.get_or_create_collection(
    name="research_papers"
)


def store_chunks(chunks, embeddings):
    """
    Store chunks and embeddings in ChromaDB.
    """

    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist()
    )

def search(query_embedding, top_k=5):

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    return results