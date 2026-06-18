import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# -----------------------
# LOAD ENVIRONMENT
# -----------------------
# (Kept for local development, Streamlit will ignore this safely)
load_dotenv()

# -----------------------
# CONFIGURE GEMINI
# -----------------------
# Check if running on Streamlit Cloud, otherwise fallback to local .env
if "GEMINI_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_KEY"])
else:
    genai.configure(api_key=os.getenv("GEMINI_KEY"))

# -----------------------
# LOAD MODEL
# -----------------------
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# -----------------------
# ASK AI FUNCTION
# -----------------------
def ask_ai(prompt):
    try:
        response = model.generate_content(
            prompt
        )
        return response.text
    except Exception as e:
        return (
            f"Error: {str(e)}"
        )
