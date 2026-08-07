from modules.embedding_model import model
from modules.vector_store import search


def retrieve(query):

    query_embedding = model.encode(
        query,
        convert_to_numpy=True
    )

    results = search(query_embedding)

    return results