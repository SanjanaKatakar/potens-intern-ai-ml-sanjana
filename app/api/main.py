from fastapi import FastAPI

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


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }