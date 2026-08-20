import streamlit as st
import requests

st.set_page_config(
    page_title="StudyPal",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 StudyPal Application")

api_url = "http://127.0.0.1:8000/ask"

# Get user input
question = st.text_input(label="Ask your question", placeholder="Type your question here...")

# Button to trigger the api
if st.button("Answer"):
    response = requests.post(
        api_url,
        json={"question": question}
    )

    result = response.json()
    answer = result["answer"]

    st.success(answer)
