import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# Load FAISS index
index = faiss.read_index("vectorstore/docs.index")

# Load chunks
with open("vectorstore/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Ask question
question = input("Ask a question: ")

# Convert question to embedding
query_embedding = model.encode([question])

# Search top 3 chunks
D, I = index.search(
    np.array(query_embedding, dtype="float32"),
    k=3
)

print("\n=== Retrieved Chunks ===\n")

for rank, idx in enumerate(I[0], start=1):
    print(f"Result {rank}:")
    print(chunks[idx])
    print("-" * 50)
