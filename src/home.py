import streamlit as st
from gpt_wrapper import generate_text, generate_image

# title of the app
st.title("Welcome to my first LLM requests")

# Header for the openai wrapper
st.header("OpenAI API")

# text box for prompt
open_ai_prompt = st.text_input("Enter your prompt")

# button to send the prompt
if st.button("Send"):  # check wether the button for our prompt is clicked
    # gpt method
    generate_text(open_ai_prompt)
    # success message
    st.sucess("Content generated successfully")
else:
    # error message if prompt is not entered.
    # st.error("Content generation failed")
    st.warning("Please insert a prompt")

st.divider()

st.header("Gemini API")
# variable to store the prompt
geminia_prompt = st.text_input("Enter your prompt", key=1)
# input the number of tokens
geminia_tokens = st.number_input(
    "Enter the number of tokens", min_value=1, max_value=200
)
if st.button("Send", key=2):
    # gemini method
    st.success("Content generated successfully")
else:
    st.warning("Please insert a prompt")
