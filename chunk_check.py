from langchain_text_splitters import RecursiveCharacterTextSplitter

with open("data/extracted.md", "r", encoding="utf-8") as f:
    text = f.read()

splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)

chunks = splitter.split_text(text)

print(f"Total chunks: {len(chunks)}")

for i, chunk in enumerate(chunks[:3]):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk)
