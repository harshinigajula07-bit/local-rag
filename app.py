import streamlit as st
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from llama_cpp import Llama

# Load once
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("vectorstore/docs.index")

with open("vectorstore/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

llm = Llama(
    model_path="models/TinyLlama-1.1B-Chat-v1.0.Q4_K_M.gguf",
    n_ctx=2048,
    verbose=False
)

question = st.text_input("Ask a question")

if st.button("Submit"):

    query_embedding = embed_model.encode([question])

    D, I = index.search(
        np.array(query_embedding, dtype="float32"),
        k=3
    )

    context = "\n\n".join(chunks[idx] for idx in I[0])

    st.subheader("Retrieved Context")
    st.write(context)

    prompt = f"""
Use the context below to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm(
        prompt,
        max_tokens=200,
        temperature=0.1
    )

    answer = response["choices"][0]["text"]

    st.subheader("Answer")
    st.write(answer)
import streamlit as st

st.title("Local RAG Test")

question = st.text_input("Ask a question")

if st.button("Submit"):
    st.write("You asked:", question)
