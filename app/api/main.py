from fastapi import FastAPI

from app.models.request_models import QuestionRequest
from app.models.response_models import QuestionResponse

from app.rag.retriever import retrieve_chunks
from app.rag.generator import generate_answer
from app.rag.citation import generate_citations

from app.rag.setup_db import setup_database
from fastapi import UploadFile

import shutil


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

@app.post("/upload")

def upload_pdf(file: UploadFile):

    save_path = f"data/raw/{file.filename}"

    with open(save_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    setup_database(save_path)

    return {
        "message": f"{file.filename} uploaded successfully"
    }