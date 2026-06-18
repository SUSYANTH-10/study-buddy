import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load local environment if present (used for local testing)
load_dotenv()

# Safe fallback logic to look up your key without crashing Streamlit
api_key = None

try:
    # Try reading from Streamlit Secrets first
    if hasattr(st, "secrets") and "GEMINI_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_KEY"]
except Exception:
    pass

# If Streamlit secrets didn't have it, check local environment (.env)
if not api_key:
    api_key = os.getenv("GEMINI_KEY")

# -----------------------
# CONFIGURE GEMINI FOR AQ. KEYS
# -----------------------
if api_key:
    genai.configure(client_options={"api_key": api_key})
else:
    # Safe fallback if no key is found at all so the app doesn't freeze
    print("Warning: No GEMINI_KEY found anywhere!")

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
    if not api_key:
        return "Error: Gemini API key is missing. Please add GEMINI_KEY to Streamlit Secrets."
        
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
