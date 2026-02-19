import os
import subprocess
import sys

# КЕРЕКТІ КІТАПХАНАНЫ АВТОМАТТЫ ОРНАТУ
try:
    import google.generativeai as genai
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", "google-generativeai"])
    import google.generativeai as genai

import streamlit as st

# API кілтің
genai.configure(api_key="AIzaSyBBj0iZFbTuj8cGWGu4Q_iiYG9kzWJIZr0")

st.title("🤖 AI Ұстаз (Дайын)")

prompt = st.text_input("Сұрақ жазыңыз (мысалы: Сәлем):")

if st.button("Жауап алу"):
    if prompt:
        with st.spinner("Ойланып жатырмын..."):
            try:
                # Тұрақты модель
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(prompt)
                st.success(response.text)
            except Exception as e:
                st.error(f"Қате: {e}")
