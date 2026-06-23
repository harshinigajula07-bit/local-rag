import streamlit as st
import fitz

st.title("PDF Question Answering System")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:
    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    st.success("PDF uploaded successfully!")

    question = st.text_input("Ask a question")

    if st.button("Submit"):
        if question:
            st.subheader("Question")
            st.write(question)

            st.subheader("PDF Content Preview")
            st.write(text[:2000])

            st.info(
                "This version extracts PDF text. "
                "To generate intelligent answers, connect a hosted LLM API."
            )
