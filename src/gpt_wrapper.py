from openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv
from pathlib import Path
import requests

# Load the environment variables
dotenv_path = Path("./.env")
load_dotenv(dotenv_path=dotenv_path)


# Function to check and return the OpenAI API client
def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("No OpenAI API key found. Please set your API key.")
        return None
    return OpenAI(api_key=api_key)


# connect to the OpenAI API
client = get_openai_client()


# Define a function that takes a prompt and returns the completions
def generate_text(prompt):
    completions = client.chat.completions.create(
        model="gpt-4o", messages=[{"role": "user", "content": prompt}]
    )
    st.write(completions.choices[0].message.content)


def generate_image(promt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=promt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url

    image_response = requests.get(image_url)
    # save image to file
    with open("two_robots_reading.jpg", "wb") as f:
        f.write(image_response.content)


# Define the Streamlit app
def main():
    st.title("GPT-4o Chatbot")
    prompt = st.text_area("Enter your message:")
    if st.button("Send"):
        response = generate_text(prompt)
        st.write(response)


generate_image("two robots reading books")


if __name__ == "__main__":
    main()
