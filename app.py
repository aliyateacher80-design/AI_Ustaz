import streamlit as st
import google.generativeai as genai

# ОСЫ ТЫРНАҚШАНЫҢ ІШІНЕ ӨЗ КІЛТІҢДІ САЛ
genai.configure(api_key="AIzaSy...ОСЫ_ЖЕРГЕ_КІЛТТІ_ҚОЙ")

st.title("🤖 Ақылды Робот-Ұстаз")
model = genai.GenerativeModel('gemini-1.5-flash')

prompt = st.text_input("Сұрағыңды жаз:")
if st.button("Жауап ал"):
    if prompt:
        response = model.generate_content(prompt)
        st.success(response.text)
