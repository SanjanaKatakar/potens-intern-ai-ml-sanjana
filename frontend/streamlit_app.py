import streamlit as st

st.set_page_config(
    page_title="RAG System",
    layout="wide"
)

st.title("📚 Multilingual RAG System")

st.write("Upload documents and ask questions.")

uploaded_files = st.file_uploader(
    "Upload Documents",
    accept_multiple_files=True
)

question = st.text_input("Ask your question")

if st.button("Submit"):
    if question:
        st.success(f"Question received: {question}")
    else:
        st.warning("Please enter a question.")