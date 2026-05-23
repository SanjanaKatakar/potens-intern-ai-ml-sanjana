from fastapi import FastAPI

from app.models.request_models import QuestionRequest
from app.models.response_models import QuestionResponse

from app.rag.retriever import retrieve_chunks
from app.rag.generator import generate_answer
from app.rag.citation import generate_citations

from app.rag.setup_db import setup_database

setup_database()

app = FastAPI(
    title="RAG System",
    description="Non-hallucinating multilingual RAG API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "RAG system is running successfully"
    }


@app.post("/ask", response_model=QuestionResponse)
def ask_question(request: QuestionRequest):

    retrieved_chunks = retrieve_chunks(
        request.question
    )

    answer = generate_answer(
        request.question,
        retrieved_chunks
    )

    citations = generate_citations(
        retrieved_chunks
    )

    return {
        "answer": answer,
        "citations": citations
    }