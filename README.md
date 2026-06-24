# Local RAG - Document Question Answering System

## Overview

Local RAG (Retrieval-Augmented Generation) is a document-based Question Answering system that allows users to upload documents and ask questions about their content. The system extracts text from documents, retrieves the most relevant information, and generates answers using a lightweight local language model.

This project follows a local-first approach, ensuring that document processing and question answering can be performed without relying on external cloud services.

---

## Features

- Upload PDF documents
- Extract text from documents
- Create document embeddings
- Store embeddings in a FAISS vector database
- Retrieve relevant document chunks
- Generate answers using a local LLM (TinyLlama via Llama.cpp)
- Simple Streamlit-based user interface
- Privacy-friendly local processing

---

## Tech Stack

### Frontend
- Streamlit

### Document Processing
- PyMuPDF (fitz)

### Embeddings
- Sentence Transformers
- all-MiniLM-L6-v2

### Vector Database
- FAISS

### Language Model
- TinyLlama
- Llama.cpp

### Programming Language
- Python

---

## Project Structure

```text
local-rag/
│
├── app.py
├── ingest.py
├── rag.py
├── rag_chat.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── sample.pdf
│   └── extracted.md
│
├── vectorstore/
│   ├── docs.index
│   └── chunks.pkl
│
├── models/
│   └── TinyLlama-1.1B-Chat-v1.0.Q4_K_M.gguf
│
└── translations/
    ├── en.py
    ├── hi.py
    └── te.py
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/harshinigajula07-bit/local-rag.git
cd local-rag
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Linux/Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Download TinyLlama Model

Download:

```text
TinyLlama-1.1B-Chat-v1.0.Q4_K_M.gguf
```

Place it inside:

```text
models/
```

---

## Build the Vector Store

Run:

```bash
python ingest.py
```

This will:

1. Extract text from PDF files
2. Split text into chunks
3. Generate embeddings
4. Store vectors in FAISS

---

## Run the Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## Workflow

1. Upload a PDF document
2. Extract document text
3. Generate embeddings
4. Store vectors in FAISS
5. Ask a question
6. Retrieve relevant document chunks
7. Generate an answer using TinyLlama
8. Display the response

---

## Example Questions

- What is the main topic of this document?
- Summarize the uploaded PDF.
- What are the key findings?
- Explain the methodology discussed.

---

## Advantages

- Local-first architecture
- Privacy-preserving
- No dependency on external APIs
- Lightweight and cost-effective
- Fast retrieval using FAISS

---

## Future Enhancements

- Multi-document support
- OCR for scanned PDFs
- Chat history
- Multilingual question answering
- Improved retrieval ranking
- Support for larger language models

---

## Author

**Harshini Gajula**

GitHub:
https://github.com/harshinigajula07-bit

---

## License

This project is developed for educational and research purposes.
