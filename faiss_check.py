import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# Read extracted text
with open("data/extracted.md", "r", encoding="utf-8") as f:
    text = f.read()

# Simple chunking
chunk_size = 300
chunks = []

for i in range(0, len(text), chunk_size):
    chunks.append(text[i : i + chunk_size])

# Generate embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks)

# Create FAISS index
vectors = np.array(embeddings, dtype="float32")

index = faiss.IndexFlatL2(vectors.shape[1])
index.add(vectors)

# Save index
faiss.write_index(index, "vectorstore/docs.index")

# Save chunks
with open("vectorstore/chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("✅ FAISS index created")
print("✅ Chunks saved")
print("Total vectors:", index.ntotal)
