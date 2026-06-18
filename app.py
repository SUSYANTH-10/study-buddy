import streamlit as st
from pypdf import PdfReader
from helper import ask_ai


# -----------------------
# PAGE CONFIG
# -----------------------

st.set_page_config(
    page_title="I Study Buddy",
    page_icon="📚"
)

st.title("📚 I Study Buddy")

st.write(
    "Upload your notes and study smarter."
)


# -----------------------
# READ PDF
# -----------------------

def read_pdf(file):

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:

        text += (
            page.extract_text()
            or ""
        )

    return text


# -----------------------
# FILE UPLOAD
# -----------------------

uploaded_file = st.file_uploader(
    "Upload PDF Notes",
    type=["pdf"]
)


# -----------------------
# MAIN APP
# -----------------------

if uploaded_file:

    notes = read_pdf(
        uploaded_file
    )

    # Prevent token overload
    notes = notes[:15000]

    st.success(
        "PDF Loaded ✅"
    )

    tab1, tab2, tab3 = st.tabs(
        [
            "💬 Ask",
            "📝 Quiz",
            "📚 Summary"
        ]
    )

    # ==========================
    # ASK QUESTIONS
    # ==========================

    with tab1:

        st.subheader(
            "Ask Questions"
        )

        question = st.text_input(
            "Ask your notes"
        )

        if st.button(
            "Get Answer"
        ):

            with st.spinner(
                "Thinking..."
            ):

                prompt = f"""
You are a study assistant.

Answer ONLY using these notes.

Notes:
{notes}

Question:
{question}

Answer briefly.
"""

                answer = ask_ai(
                    prompt
                )

            st.subheader(
                "Answer"
            )

            st.write(
                answer
            )

    # ==========================
    # QUIZ
    # ==========================

    with tab2:

        st.subheader(
            "Generate Quiz"
        )

        if st.button(
            "Generate Quiz"
        ):

            with st.spinner(
                "Creating quiz..."
            ):

                quiz_prompt = f"""
Generate ONLY:

3 MCQs

Include:
- Question
- 4 options
- Correct answer

Use ONLY these notes:

{notes}
"""

                quiz = ask_ai(
                    quiz_prompt
                )

            st.write(
                quiz
            )

    # ==========================
    # SUMMARY
    # ==========================

    with tab3:

        st.subheader(
            "Generate Summary"
        )

        if st.button(
            "Generate Summary"
        ):

            with st.spinner(
                "Summarizing..."
            ):

                summary_prompt = f"""
Create:

1. Short summary

2. Important points

3. Revision notes

Use ONLY these notes:

{notes}
"""

                summary = ask_ai(
                    summary_prompt
                )

            st.write(
                summary
            )

            st.download_button(
                label="⬇ Download Summary",
                data=summary,
                file_name="study_summary.txt",
                mime="text/plain"
            )