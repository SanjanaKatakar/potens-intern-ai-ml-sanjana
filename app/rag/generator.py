import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

print("\nAPI KEY FOUND:", api_key is not None)

client = Groq(
    api_key=api_key
)


def generate_answer(question, retrieved_chunks):

    context = "\n\n".join(
        [
            f"[Page {chunk['page']}]\n{chunk['text']}"
            for chunk in retrieved_chunks
        ]
    )

    prompt = f"""
Answer ONLY using the provided context.

If answer is not present, say:
"The documents do not contain enough information."

QUESTION:
{question}

CONTEXT:
{context}

ANSWER:
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        answer = response.choices[0].message.content

        return answer

    except Exception as e:

        print("\nGROQ ERROR:\n")
        print(e)

        return "Error generating answer."