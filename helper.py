import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load local environment if present
load_dotenv()

# Safe fallback logic to look up your key
api_key = None
try:
    if hasattr(st, "secrets") and "GEMINI_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_KEY"]
except Exception:
    pass

if not api_key:
    api_key = os.getenv("GEMINI_KEY")

# -----------------------
# ASK AI FUNCTION (Direct Key Passing)
# -----------------------
def ask_ai(prompt):
    if not api_key:
        return "Error: Gemini API key is missing. Please add GEMINI_KEY to Streamlit Secrets."
        
    try:
        # We pass the api_key DIRECTLY into the model creation here
        # This completely bypasses the broken genai.configure() step!
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            api_key=api_key
        )
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
