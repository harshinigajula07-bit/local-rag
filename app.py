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

# Set up the title of the app
st.title("PDF Question Answering App")

# 1. Create the file uploader widget specifically for PDFs
uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])

# Check if a file has been uploaded
if uploaded_file is not None:
    # Success message showing the file name
    st.success(f"Successfully uploaded: {uploaded_file.name}")
    
# 2. The single question and submit layout at the bottom
user_question = st.text_input("Ask a question", key="pdf_user_question")

if st.button("Submit", key="pdf_submit_button"):
    if uploaded_file is not None and user_question:
        st.write(f"Processing your question: '{user_question}' based on {uploaded_file.name}...")
        # Your PDF processing / AI RAG model logic will go here
    elif uploaded_file is None:
        st.warning("Please upload a PDF file first!")
    else:
        st.warning("Please enter a question before submitting.")
