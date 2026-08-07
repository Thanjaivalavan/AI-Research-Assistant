from modules.pdf_loader import extract_text_from_pdf
from modules.text_cleaner import clean_text
from modules.document_indexer import index_document
from modules.retriever import retrieve
from modules.prompt_builder import build_prompt
from modules.llm import generate_answer
import streamlit as st

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚",
    layout="wide"
)

# -----------------------------------
# Title
# -----------------------------------
st.title("📚 AI Research Assistant")

st.markdown(
    """
Welcome to the AI Research Assistant.

This application will help you:

- Upload research papers
- Ask questions
- Retrieve relevant information
- Generate answers with citations
"""
)

# -----------------------------------
# Sidebar
# -----------------------------------
with st.sidebar:

    st.header("Project")

    st.write("Phase 1")

    st.write("Module 1")

    st.write("Milestone 2")

    st.divider()

    uploaded_files = st.file_uploader(
        "Upload Research Papers",
        type=["pdf"],
        accept_multiple_files=True
    )
    
    if uploaded_files:

        st.success(f"{len(uploaded_files)} PDF(s) uploaded")

        for pdf in uploaded_files:

            st.write("📄", pdf.name)
            st.write(f"Size: {round(pdf.size / 1024, 2)} KB")
            st.divider()
    
    st.divider()

    st.info(
        "Currently only the UI is implemented."
    )

# -----------------------------------
# Main Section
# -----------------------------------

if uploaded_files:

    for pdf in uploaded_files:

        with st.spinner(f"Indexing {pdf.name}..."):

            index_document(pdf)

        st.success(f"{pdf.name} indexed successfully.")

st.subheader("Ask a Question")

question = st.text_area(
    "Enter your research question",
    height=120
)

ask_button = st.button(
    "Ask"
)

st.divider()

st.subheader("Response")

if ask_button:

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Thinking..."):

            # Step 1: Retrieve relevant chunks
            results = retrieve(question)

            # Step 2: Extract retrieved documents
            documents = results["documents"][0]

            # Step 3: Build prompt
            prompt = build_prompt(
                question,
                documents
            )

            # Step 4: Generate answer
            answer = generate_answer(prompt)

        st.subheader("Answer")

        st.write(answer)

else:

    st.info("Ask a question to begin.")