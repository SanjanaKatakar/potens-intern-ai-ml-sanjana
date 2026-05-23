from app.rag.loader import load_pdf
from app.rag.chunker import chunk_text

PDF_PATH = "data/raw/sample.pdf"

documents = load_pdf(PDF_PATH)

all_chunks = []

for doc in documents:

    chunks = chunk_text(doc["text"])

    for chunk in chunks:

        all_chunks.append({
            "page": doc["page"],
            "chunk": chunk
        })

print(f"\nTotal chunks created: {len(all_chunks)}")

print("\n================ SAMPLE CHUNK ================\n")

print(all_chunks[0])