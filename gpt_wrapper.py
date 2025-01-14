from openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path("../src/.env")
load_dotenv(dotenv_path=dotenv_path)

# Load the environment variables
# load_dotenv()


# Function to check and return the OpenAI API client
def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("No OpenAI API key found. Please set your API key.")
        return None
    return OpenAI(api_key=api_key)


# Create an instance of the OpenAI class
# api_key = st.secrets[openai_api_key]

# connect to the OpenAI API
client = get_openai_client()


# Define a function that takes a prompt and returns the completions
def get_completions(prompt):
    completions = client.chat.completions.create(
        model="gpt-4o", messages=[{"role": "user", "content": prompt}]
    )
    return completions.choices[0].message.content


# Define the Streamlit app
def main():
    st.title("GPT-4o Chatbot")
    prompt = st.text_area("Enter your message:")
    if st.button("Send"):
        response = get_completions(prompt)
        st.write(response)


if __name__ == "__main__":
    main()
