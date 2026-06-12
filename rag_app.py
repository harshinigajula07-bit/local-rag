import streamlit as st

from translations.en import translations as en
from translations.te import translations as te
from translations.hi import translations as hi
language = st.sidebar.selectbox(
    "Choose Language",
    ["English", "Telugu", "Hindi"]
)

if language == "English":
    t = en
elif language == "Telugu":
    t = te
else:
    t = hi

st.title("AI Healthcare Information Assistant")
st.title(t["title"])

st.file_uploader("Upload PDF")
st.file_uploader(t["upload"], key="upload1")

st.text_input("Ask a question")
st.text_input(t["question"], key="q1")
