import google.generativeai as genai
import streamlit as st


def generate_content(prompt, tokens):
    genai.configure(api_key="api_key")
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    response = model.generate_content(
        prompt,
        generation_config=genai.GenerationConfig(max_tokens=tokens, temperature=0.1),
    )
    st.write(response.text)
