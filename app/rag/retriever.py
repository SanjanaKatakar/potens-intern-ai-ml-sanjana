from app.rag.embeddings import get_embedding
from app.rag.vectordb import collection
from app.rag.translator import translate_to_english


def retrieve_chunks(query, top_k=10):
    """
    Retrieve most relevant chunks.
    """

    translated_query = translate_to_english(query)

    query_embedding = get_embedding(
        [translated_query]
    )[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    retrieved_docs = []

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    for doc, metadata in zip(
        documents,
        metadatas
    ):

        if len(doc.strip()) > 100:

            retrieved_docs.append({
                "text": doc,
                "page": metadata["page"]
            })

    return retrieved_docs