# Multilingual RAG System with FastAPI and Streamlit

## Project Overview

This project is a multilingual Retrieval-Augmented Generation (RAG) system built using FastAPI, Streamlit, ChromaDB, Sentence Transformers, and Groq LLMs.

The system allows users to:

- Upload PDF documents dynamically
- Process and index documents automatically
- Ask questions in multiple languages
- Retrieve semantically relevant chunks
- Generate grounded answers using retrieved context
- Reduce hallucinations using context-constrained prompting
- Display citations from source documents

The application is designed as a lightweight and efficient AI-powered document question-answering system.

---

# Features

- Dynamic PDF Upload
- Automatic Document Chunking
- Semantic Search using Embeddings
- ChromaDB Vector Storage
- FastAPI Backend
- Streamlit Frontend
- Multilingual Query Support
- Citation-Based Responses
- Hallucination Reduction
- Grounded Answer Generation

---

# Tech Stack

| Component | Technology |
|---|---|
| Backend | FastAPI |
| Frontend | Streamlit |
| Vector Database | ChromaDB |
| Embedding Model | sentence-transformers/all-MiniLM-L6-v2 |
| LLM | Groq Llama 3.3 70B |
| PDF Processing | PyMuPDF |
| Translation | deep-translator |
| Language | Python |

---

# System Architecture

```text
User Question
      ↓
Streamlit Frontend
      ↓
FastAPI Backend
      ↓
Multilingual Translation
      ↓
Semantic Retrieval
      ↓
ChromaDB Vector Search
      ↓
Relevant Chunks
      ↓
Groq LLM
      ↓
Grounded Answer + Citations
```

---

# Folder Structure

```text
potens-intern-ai-ml-sanjana/

├── app/
│   ├── api/
│   ├── rag/
│   ├── models/
│   └── core/
│
├── frontend/
│   └── streamlit_app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
├── tests/
│
├── requirements.txt
├── README.md
├── AI_USAGE.md
└── .env
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/SanjanaKatakar/potens-intern-ai-ml-sanjana.git
```

---

# Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# Run FastAPI Backend

```bash
uvicorn app.api.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

Swagger API Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Run Streamlit Frontend

```bash
streamlit run frontend/streamlit_app.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

# How It Works

## 1. PDF Upload

Users upload PDF documents through the Streamlit interface.

---

## 2. Document Processing

The system:
- extracts text from PDFs
- preserves page information
- creates overlapping chunks

---

## 3. Embedding Generation

Each chunk is converted into vector embeddings using Sentence Transformers.

---

## 4. Vector Storage

Embeddings are stored in ChromaDB for semantic retrieval.

---

## 5. Retrieval

User queries are:
- translated to English if needed
- embedded into vectors
- matched semantically against stored chunks

---

## 6. Grounded Answer Generation

Relevant chunks are passed to Groq LLM with strict prompting rules to reduce hallucinations.

---

## 7. Citation Generation

The system returns source page references and snippets from retrieved chunks.

---

# Hallucination Reduction Strategy

The system minimizes hallucinations using:

- Retrieval-Augmented Generation (RAG)
- Context-constrained prompting
- Citation-based answering
- Semantic retrieval
- Multilingual query translation
- Strict fallback responses when information is missing

---

# Example Queries

```text
How can hallucinations in LLMs be reduced?
```

```text
LLM hallucination kaise reduce hota hai?
```

```text
हैलुसिनेशन कैसे कम किया जाता है?
```

---

# Future Improvements

- Hybrid Retrieval (BM25 + Vector Search)
- Reranking Models
- Multiple Document Collections
- Conversation Memory
- Better UI Design
- Confidence Estimation
- OCR Support for Scanned PDFs

---

# Author

Sanjana Katkar

---