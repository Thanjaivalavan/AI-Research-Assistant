from modules.pdf_loader import extract_text_from_pdf
from modules.text_cleaner import clean_text
from modules.text_chunker import chunk_text

from modules.embedding_model import generate_embeddings
from modules.vector_store import store_chunks


def index_document(uploaded_file):

    raw_text = extract_text_from_pdf(uploaded_file)

    cleaned_text = clean_text(raw_text)

    chunks = chunk_text(cleaned_text)

    embeddings = generate_embeddings(chunks)

    store_chunks(
        chunks,
        embeddings
    )

    return True