import streamlit as st
import os

# 1. КЕРЕКТІ ҚҰРАЛДАРДЫ МӘЖБҮРЛІ ТҮРДЕ ЖАҢАРТУ
import subprocess
import sys

def install_latest_gemini():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "google-generativeai"])

try:
    import google.generativeai as genai
except ImportError:
    install_latest_gemini()
    import google.generativeai as genai

# 2. БАЙЛАНЫСТЫ ОРНАТУ
genai.configure(api_key="AIzaSyBBj0iZFbTuj8cGWGu4Q_iiYG9kzWJIZr0")

st.title("🤖 AI Ұстаз: Жеңіс жақын!")

# Сұрақ жазу
prompt = st.text_input("Сұрағыңызды осында жазыңыз:")

if st.button("Жауап алу"):
    if prompt:
        with st.spinner("Миымды жаңартып, ойланып жатырмын..."):
            try:
                # ЕҢ ТҰРАҚТЫ МОДЕЛЬ
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(prompt)
                
                st.write("---")
                st.success(response.text)
                st.balloons()
            except Exception as e:
                # Егер тағы қате шықса, ең сенімді модельге көшу
                try:
                    model = genai.GenerativeModel('gemini-pro')
                    response = model.generate_content(prompt)
                    st.success(response.text)
                except:
                    st.error(f"Қате: {e}")
                    st.info("Бетті жаңартып (Refresh), 1 минуттан соң қайта байқаңыз.")
