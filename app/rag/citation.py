def generate_citations(retrieved_chunks):
    """
    Generate citations from retrieved chunks.
    """

    citations = []

    for chunk in retrieved_chunks:

        citations.append({
            "page": chunk["page"],
            "snippet": chunk["text"][:200]
        })

    return citations