import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from llama_cpp import Llama

# Load embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("vectorstore/docs.index")

# Load chunks
with open("vectorstore/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

# Load TinyLlama model
llm = Llama(
    model_path="models/TinyLlama-1.1B-Chat-v1.0.Q4_K_M.gguf",
    n_ctx=2048,
    verbose=False
)

while True:
    question = input("\nAsk a question (or 'exit'): ")

    if question.lower() == "exit":
        break

    # Create query embedding
    query_embedding = embed_model.encode([question])

    # Search top 3 chunks
    D, I = index.search(
        np.array(query_embedding, dtype="float32"),
        k=5
    )

    # Build context
    context = "\n\n".join(chunks[idx] for idx in I[0])

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

    answer = response["choices"][0]["text"].strip()

    print("\nAnswer:")
    print(answer)
