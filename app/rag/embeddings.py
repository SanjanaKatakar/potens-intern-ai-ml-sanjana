from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


def get_embedding(texts):
    """
    Generate embeddings for text chunks.
    """

    return embedding_model.encode(texts).tolist()