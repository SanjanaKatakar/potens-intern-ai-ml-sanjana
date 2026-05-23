from app.rag.embeddings import get_embedding
from app.rag.vectordb import collection


def retrieve_chunks(query, top_k=5):
    """
    Retrieve most relevant chunks from ChromaDB.
    """

    query_embedding = get_embedding([query])[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    retrieved_docs = []

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for doc, metadata, distance in zip(
        documents,
        metadatas,
        distances
    ):

        retrieved_docs.append({
            "text": doc,
            "page": metadata["page"],
            "score": distance
        })

    return retrieved_docs