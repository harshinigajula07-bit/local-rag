from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

with open("data/extracted.md", "r", encoding="utf-8") as f:
    text = f.read()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = splitter.split_text(text)

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(chunks)

print("Number of chunks:", len(chunks))
print("Embedding shape:", embeddings.shape)
