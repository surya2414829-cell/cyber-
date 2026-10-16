import streamlit as st
from google import genai
from pathlib import Path

st.set_page_config(page_title="Cyber Rakshak", page_icon="🛡️")

stylesheet = Path(__file__).with_name("style.css").read_text(encoding="utf-8")
st.markdown(f"<style>{stylesheet}</style>", unsafe_allow_html=True)

st.title("🛡️ Cyber Rakshak - Gemma")
st.write("Nenu Surya chesina Cyber Safety App!")

with st.sidebar:
    st.header("Gemma Setup")
    api_key = st.text_input("Gemini API key", type="password")

user_input = st.text_input("Nee doubt adugu (Eg: Phishing ante enti?)")

if st.button("Adugu 🛡️", type="primary"):
    if user_input:
        if not api_key:
            st.warning("Paste your Gemini API key in the sidebar to generate an answer.")
        else:
            prompt = (
                "You are Cyber Rakshak, a friendly cyber safety expert for Indian users. "
                "Answer briefly in a Telugu and English mix. Give practical, careful advice "
                f"for this question: {user_input}\nEnd with: If this is fraud, call 1930."
            )
            try:
                client = genai.Client(api_key=api_key)
                with st.spinner("Gemma is preparing an answer..."):
                    response = client.models.generate_content(
                        model="gemma-3-12b-it",
                        contents=prompt,
                    )
                if response.text:
                    st.markdown(response.text)
                else:
                    st.warning("Gemma returned an empty response. Please try again.")
            except Exception as error:
                st.error(f"Could not generate an answer: {error}")
    else:
        st.warning("Question type chey mundu!")

st.write("---")
st.write("Developed by Surya - Vijayawada 2026")