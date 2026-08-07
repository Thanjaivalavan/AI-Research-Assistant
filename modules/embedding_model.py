from sentence_transformers import SentenceTransformer

# Load only once when the application starts
model = SentenceTransformer("paraphrase-MiniLM-L3-v2")


def generate_embeddings(chunks):
    """
    Generate embeddings for a list of text chunks.
    """

    embeddings = model.encode(
        chunks,
        convert_to_numpy=True,
        show_progress_bar=False
    )

    return embeddings