import streamlit as st

st.title("Deployment Test")

st.success("Streamlit Cloud is working!")

question = st.text_input("Ask a question")

if st.button("Submit"):
    st.write("You asked:", question)
