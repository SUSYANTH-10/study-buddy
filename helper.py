import google.generativeai as genai
import os

from dotenv import load_dotenv


# -----------------------
# LOAD ENVIRONMENT
# -----------------------

load_dotenv()


# -----------------------
# CONFIGURE GEMINI
# -----------------------

genai.configure(
    api_key=os.getenv(
        "GEMINI_KEY"
    )
)


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