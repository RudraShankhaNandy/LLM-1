import os
import streamlit as st
import requests
from dotenv import load_dotenv
from speech_to_text import listen_continuous
from text_to_speech import synthesize_text

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "api")
api_port = int(os.environ.get("PORT", 8080))


# Streamlit UI elements
st.title("Dropbox Search Tool")

k = listen_continuous()

question = st.text_input(
    "Search for something",
    placeholder="What data are looking for?"
)
question = k

if question:
    url = f'http://{api_host}:{api_port}/'
    data = {"query": question}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        st.write("### Answer")
        st.write(response.json())
        synthesize_text(response.json(),'output.mp3')
    else:
        st.error(f"Failed to send data to Pathway API. Status code: {response.status_code}")
