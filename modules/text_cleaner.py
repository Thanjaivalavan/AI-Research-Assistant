import re


def clean_text(text: str) -> str:
    """
    Basic text cleaning for research papers.
    """

    # Replace tabs with spaces
    text = text.replace("\t", " ")

    # Remove multiple spaces
    text = re.sub(r" +", " ", text)

    # Remove multiple blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove spaces before newline
    text = re.sub(r" *\n", "\n", text)

    # Remove leading and trailing whitespace
    text = text.strip()

    return text