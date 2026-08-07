def build_prompt(question, retrieved_chunks):
    """
    Build a RAG prompt using retrieved context.
    """

    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are an AI Research Assistant.

Answer in very simple grammar.

If the answer is not present in the context,
say:
"I don't know. Please refer to the provided context for more information."

Question:
{question}

Answer:
"""

    return prompt