from app.rag.retriever import retrieve_chunks

query = "How can hallucinations in LLMs be reduced?"

results = retrieve_chunks(query)

print("\n=========== RETRIEVED CHUNKS ===========\n")

for idx, result in enumerate(results):

    print(f"\nRESULT {idx + 1}")
    print(f"Page: {result['page']}")
    print(f"Score: {result['score']}")

    print("\nText:")
    print(result["text"][:500])