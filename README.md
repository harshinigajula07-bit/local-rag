# 🩺 AI Healthcare Assistant

An AI-powered Healthcare Information Assistant built using **Streamlit**, **LangChain**, **ChromaDB**, and **Ollama**. The application allows users to upload PDF documents, ask questions, and receive context-aware answers using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- 📄 Upload healthcare-related PDF documents
- 🤖 Ask questions about uploaded documents
- 🧠 Local AI Inference using Ollama
- 🔍 Semantic Search with ChromaDB
- 🌐 Multilingual Response Support
- 🔑 Ready for BYOK (Bring Your Own Key) integration
- 💻 Interactive Streamlit Web Interface

---

## 🏗️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **AI Framework:** LangChain
- **Vector Database:** ChromaDB
- **Document Processing:** PyPDF
- **Local LLM:** Ollama (Phi, Llama, Mistral)
- **Embeddings:** Nomic Embed Text

---

## 📂 Project Structure

```text
ai-healthcare-assistant/
│
├── app.py
├── rag.py
├── uploads/
├── vectorstore/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-healthcare-assistant.git
cd ai-healthcare-assistant
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download and install Ollama:

https://ollama.com/download

Verify installation:

```bash
ollama --version
```

### 5. Pull Required Models

```bash
ollama pull phi
ollama pull nomic-embed-text
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open in browser:

```text
http://localhost:8501
```

---

## 🔄 Workflow

1. Upload a PDF document.
2. The document is split into chunks.
3. Chunks are converted into embeddings.
4. Embeddings are stored in ChromaDB.
5. User asks a question.
6. Relevant information is retrieved.
7. Ollama generates an answer using the retrieved context.

---

## 🌟 Future Enhancements

- Voice Input and Output
- Chat History
- Multiple PDF Support
- Cloud Deployment
- BYOK Support (OpenAI, Gemini, Claude)
- Enhanced Multilingual Support

---

## 🎯 Objective

To provide an AI-powered healthcare information assistant that combines document retrieval and local language models for secure, efficient, and intelligent document-based question answering.

---

## 👩‍💻 Author

**Harshini Gajula**

Built as a RAG-based AI application using Streamlit and Ollama.
