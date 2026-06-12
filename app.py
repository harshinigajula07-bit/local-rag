import streamlit as st
import os
from rag import load_pdf, create_db, search


os.makedirs("uploads", exist_ok=True)
os.makedirs("vectorstore", exist_ok=True)

st.title("🩺 AI Healthcare Assistant")

uploaded_file = st.file_uploader("Upload PDF")

if uploaded_file:
    path = f"uploads/{uploaded_file.name}"

    with open(path, "wb") as f:
        f.write(uploaded_file.read())

    docs = load_pdf(path)
    db = create_db(docs)

    query = st.text_input("Ask a question")

    if query:
        docs = search(db, query)
        context = " ".join([d.page_content for d in docs])

        response = ollama.chat(
            model="phi",
            messages=[{
                "role": "user",
                "content": f"""
        You are a helpful AI assistant.

        IMPORTANT RULE:
        - Always answer ONLY in {st.session_state.language}
        - Do NOT respond in English unless language is English
        - Keep answers simple and clear

        Context:
        {context}

        Question:
        {query}
        """
            }]
        )

        st.write("### Answer")
        st.write(response["message"]["content"])
import streamlit as st

st.set_page_config(
    page_title="AI Healthcare Assistant",
    page_icon="🩺",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "language" not in st.session_state:
    st.session_state.language = "English"

if "mode" not in st.session_state:
    st.session_state.mode = "Local (Ollama)"

# ---------------- SIDEBAR NAVIGATION ----------------
st.sidebar.title("🧠 AI Assistant Menu")

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "📄 Upload & Chat",
        "🤖 AI Mode",
        "🌐 Language Settings",
        "📚 About Project"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Built with Streamlit + Ollama + RAG 🧠")
if page == "🌐 Language Settings":
    st.title("🌍 Language Settings")

    st.session_state.language = st.selectbox(
        "Choose your language",
        [
            "English",
            "Hindi",
            "Telugu",
            "Tamil",
            "Kannada",
            "French",
            "Spanish"
        ]
    )

    st.success(f"Selected Language: {st.session_state.language}")
    st.info("AI will respond in this language (if supported by model).")
elif page == "🤖 AI Mode":
    st.title("🤖 AI Mode Selection")

    st.session_state.mode = st.radio(
        "Choose AI Mode",
        ["Local (Ollama)", "Cloud (BYOK)"]
    )

    st.success(f"Current Mode: {st.session_state.mode}")
elif page == "📄 Upload & Chat":
    st.title("📄 Chat with Documents")

    uploaded_file = st.file_uploader("Upload your PDF")

    if uploaded_file:
        st.success("File uploaded successfully!")

        query = st.text_input("Ask a question")

        if query:
            # Example context (replace with your RAG logic)
            context = "Sample context from PDF"   
            response=ollama.chat(    
                model="phi",
                messages=[{
                    "role": "user",
                    "content": f"""
Answer in {st.session_state.language}.

Context: {context}

Question: {query}
"""
                }]
            )

            st.write("### Answer")
            st.write(response["message"]["content"])
if page == "🏠 Home":
    st.title("🩺 AI Healthcare Assistant")
    st.write("""
    Welcome! This app helps you:
    - Upload medical PDFs 📄
    - Ask questions 🤖
    - Get AI answers using Ollama 🧠
    - Switch languages 🌍
    - Choose AI mode ⚙️
    """)
elif page == "📚 About Project":
    st.title("📚 About This Project")

    st.write("""
    This is a RAG-based AI system built using:

    - Streamlit (UI)
    - Ollama (Local AI)
    - ChromaDB (Vector Database)
    - LangChain (RAG pipeline)

    Features:
    ✔ PDF Q&A  
    ✔ Multilingual responses  
    ✔ Local + Cloud AI support  
    """)

elif page == "📄 Upload & Chat":
    st.title("📄 Chat with Documents")

    uploaded_file = st.file_uploader("Upload PDF")

    if uploaded_file:
        path = f"uploads/{uploaded_file.name}"

        with open(path, "wb") as f:
            f.write(uploaded_file.read())

        docs = load_pdf(path)
        db = create_db(docs)

        query = st.text_input("Ask a question")

        if query:
            docs = search(db, query)

            context = " ".join([d.page_content for d in docs])

            response = ollama.chat(
                model="phi",
                messages=[{
                    "role": "user",
                    "content": f"""
Always answer in {st.session_state.language}.

Context:
{context}

Question:
{query}
"""
                }]
            )

            st.write("### Answer")
            st.write(response["message"]["content"])
