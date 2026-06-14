import streamlit as st

from translations.en import translations as en
from translations.te import translations as te
from translations.hi import translations as hi

# Language selector
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

# Title
st.title(t["title"])

# Upload PDF
uploaded_file = st.file_uploader(
    t["upload"],
    type=["pdf"],
    key="upload1"
)

# Ask question
question = st.text_input(
    t["question"],
    key="q1"
)

# Display results
if uploaded_file:
    st.success("PDF uploaded successfully!")

if question:
    st.write("Question:", question)
