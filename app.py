import streamlit as st
import google.generativeai as genai

# API кілтің
genai.configure(api_key="AIzaSyBBj0iZFbTuj8cGWGu4Q_iiYG9kzWJIZr0")

st.title("🤖 Ақылды Ұстаз")

# Сұрақ жазатын орын
prompt = st.text_input("Сұрағыңызды жазыңыз:")

if st.button("Жауап алу"):
    if prompt:
        try:
            # Ең сенімді модель нұсқасы
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            st.write("---")
            st.success(response.text)
        except Exception as e:
            st.error(f"Қате шықты. Мынаны байқап көрейік...")
            try:
                # Егер біріншісі істемесе, екінші нұсқа
                model = genai.GenerativeModel('gemini-1.0-pro')
                response = model.generate_content(prompt)
                st.success(response.text)
            except:
                st.warning("Сервер жаңартылып жатыр. 1 минуттан соң қайталаңыз.")
