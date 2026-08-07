import fitz  # PyMuPDF


def extract_text_from_pdf(uploaded_file):
    """
    Extract text from an uploaded PDF file.

    Returns:
        text (str): Complete extracted text.
    """

    document = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    full_text = ""

    for page in document:
        full_text += page.get_text()

    document.close()

    return full_text
