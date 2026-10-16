import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Cyber Rakshak", page_icon="🛡️")

stylesheet = Path(__file__).with_name("style.css").read_text(encoding="utf-8")
st.markdown(f"<style>{stylesheet}</style>", unsafe_allow_html=True)

st.title("🛡️ Cyber Rakshak - Gemma")
st.write("Nenu Surya chesina Cyber Safety App!")

user_input = st.text_input("Nee doubt adugu (Eg: Phishing ante enti?)")

if st.button("Adugu"):
    if user_input:
        st.success(f"Nee question: {user_input}")
        st.write("**Answer:** Idi Surya develop chesina AI. Hackathon ki ready!")
        st.write("- Phishing ante fake links tho mosam cheyadam")
        st.write("- OTP evariki cheppaku")
        st.write("- Safe browsing chey")
    else:
        st.warning("Question type chey mundu!")

st.write("---")
st.write("Developed by Surya - Vijayawada 2026")