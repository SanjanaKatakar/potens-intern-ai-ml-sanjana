import requests
import streamlit as st

st.set_page_config(
    page_title="Multilingual RAG System",
    layout="wide"
)

st.title("📚 Multilingual RAG System")

st.write("Ask questions from your uploaded documents.")


question = st.text_input(
    "Enter your question"
)


if st.button("Get Answer"):

    if question.strip():

        with st.spinner("Generating answer..."):

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/ask",
                    json={
                        "question": question
                    }
                )
                
                data = response.json()

                st.subheader("Answer")

                st.write(data["answer"])

                st.subheader("Citations")

                for citation in data["citations"]:

                    st.markdown(
                        f"""
            Page: {citation['page']}

            Snippet:
            {citation['snippet']}
            """
                    )

            except Exception as e:

                st.error(f"Error: {e}")

    else:

        st.warning("Please enter a question.")