import streamlit as st
import google.generativeai as genai

# МЫНА ЖЕРГЕ ӨЗ КІЛТІҢДІ ҚОЙ ( image_2dfa01.png-дағы AIzaSy... )
genai.configure(api_key="ОСЫ_ЖЕРГЕ_КІЛТТІ_ЖАЗ")

st.title("🤖 Менің Роботым")
model = genai.GenerativeModel('gemini-1.5-flash')

prompt = st.text_input("Маған сұрақ қой:")
if st.button("Жауап ал"):
    try:
        response = model.generate_content(prompt)
        st.success(response.text)
    except Exception as e:
        st.error(f"Қате: {e}")
