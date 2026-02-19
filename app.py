import streamlit as st
import google.generativeai as genai

# Кілтті енгізу
genai.configure(api_key="AIzaSyBBj0iZFbTuj8cGWGu4Q_iiYG9kzWJIZr0")

st.title("🤖 AI Ұстаз")

prompt = st.text_input("Сұрақ жазыңыз:")

if st.button("Сұрау"):
    if prompt:
        try:
            # Тек қана ең негізгі модельді шақырамыз
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            st.success(response.text)
        except Exception as e:
            st.error(f"Қате: {e}")
