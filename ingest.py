import pymupdf4llm

pdf_path = "data/sample.pdf"

print(f"Reading PDF: {pdf_path}")

text = pymupdf4llm.to_markdown(pdf_path)

print("\n=== First 1000 Characters ===\n")
print(text[:1000])

with open("data/extracted.md", "w", encoding="utf-8") as f:
    f.write(text)

print("\n✅ PDF extracted successfully")
print("✅ Output saved to data/extracted.md")
