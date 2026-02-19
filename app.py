import streamlit as st
import google.generativeai as genai

# API кілтің
genai.configure(api_key="AIzaSyBBj0iZFbTuj8cGWGu4Q_iiYG9kzWJIZr0")

st.title("🤖 AI Ұстаз")

# Сұрақ жазатын жол
prompt = st.text_input("Сұрақ жазыңыз:")

if st.button("Жауап алу"):
    if prompt:
        try:
            # Модельді ең тұрақты нұсқада шақыру
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            st.success(response.text)
        except Exception as e:
            # Егер қате шықса, нақты не екенін көрейік
            st.error(f"Байланыс орнатылмады. Себебі: {e}")
            st.info("Ескерту: Егер '404' шықса, GitHub-та requirements.txt файлын жасау керек.")
