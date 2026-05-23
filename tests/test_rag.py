from app.rag.retriever import retrieve_chunks
from app.rag.generator import generate_answer
from app.rag.citation import generate_citations

question = "How can hallucinations in large language models be reduced?"

retrieved_chunks = retrieve_chunks(question)

answer = generate_answer(
    question,
    retrieved_chunks
)

citations = generate_citations(
    retrieved_chunks
)

print("\n=========== QUESTION ===========\n")
print(question)

print("\n=========== ANSWER ===========\n")
print(answer)

print("\n=========== CITATIONS ===========\n")

for citation in citations:

    print(f"\nPage: {citation['page']}")

    print(citation["snippet"])