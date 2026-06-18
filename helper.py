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
# ASK AI FUNCTION (Targeted Client Config)
# -----------------------
def ask_ai(prompt):
    if not api_key:
        return "Error: Gemini API key is missing. Please add GEMINI_KEY to Streamlit Secrets."
        
    try:
        # Create a specific client targeting the api_key properly
        client = genai.Client(api_key=api_key)
        
        # Request content generation through the client model manager
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text
    except Exception as e:
        # Fallback if the newer Client object is not supported by your library version
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-2.5-flash")
            response = model.generate_content(prompt)
            return response.text
        except Exception as e2:
            return f"Authentication Error: {str(e2)}"
