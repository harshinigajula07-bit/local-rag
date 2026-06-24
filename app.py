import streamlit as st
import fitz  # PyMuPDF

st.title("Local RAG - PDF Question Answering System")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    pdf_text = ""

    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    for page in pdf:
        pdf_text += page.get_text()

    st.success(f"Uploaded: {uploaded_file.name}")

    question = st.text_input("Ask a question about the PDF")

    if question:
        question_words = question.lower().split()

        matches = []

        for paragraph in pdf_text.split("\n"):
            if any(word in paragraph.lower() for word in question_words):
                matches.append(paragraph)

        st.subheader("Answer")

        if matches:
            st.write("\n".join(matches[:5]))
        else:
            st.write("No relevant information found in the PDF.")
