print("=== Verifying Installed Packages ===\n")

packages = [
    ("pymupdf4llm", "PyMuPDF4LLM"),
    ("sentence_transformers", "Sentence Transformers"),
    ("faiss", "FAISS"),
    ("llama_cpp", "Llama.cpp"),
    ("langchain", "LangChain"),
    ("langchain_community", "LangChain Community"),
    ("streamlit", "Streamlit"),
]

for module_name, display_name in packages:
    try:
        __import__(module_name)
        print(f"✅ {display_name} installed successfully")
    except ImportError as e:
        print(f"❌ {display_name} NOT installed")
        print(f"   Error: {e}")

print("\n=== Verification Complete ===")
