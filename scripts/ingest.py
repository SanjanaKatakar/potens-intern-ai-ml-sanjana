from app.rag.loader import load_pdf
from app.rag.chunker import chunk_text
from app.rag.embeddings import get_embedding
from app.rag.vectordb import collection

PDF_PATH = "data/raw/sample.pdf"

documents = load_pdf(PDF_PATH)

all_chunks = []
all_embeddings = []
all_ids = []
all_metadata = []

chunk_counter = 0

for doc in documents:

    chunks = chunk_text(doc["text"])

    for chunk in chunks:

        chunk_id = f"chunk_{chunk_counter}"

        embedding = get_embedding([chunk])[0]

        all_chunks.append(chunk)

        all_embeddings.append(embedding)

        all_ids.append(chunk_id)

        all_metadata.append({
            "page": doc["page"]
        })

        chunk_counter += 1


collection.add(
    documents=all_chunks,
    embeddings=all_embeddings,
    ids=all_ids,
    metadatas=all_metadata
)

print(f"\nStored {len(all_chunks)} chunks in ChromaDB")