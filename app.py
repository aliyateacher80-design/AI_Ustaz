import streamlit as st
import os
import subprocess
import sys

# СЕРВЕРДІ ЖАҢАРТУ (АВТОМАТТЫ ТҮРДЕ)
@st.cache_resource
def install_packages():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", "google-generativeai"])
    except:
        pass

install_packages()

import google.generativeai as genai

# API КІЛТІҢ
genai.configure(api_key="AIzaSyBBj0iZFbTuj8cGWGu4Q_iiYG9kzWJIZr0")

st.title("🤖 Менің Алғашқы Роботым")

# Сұрақ қою
prompt = st.text_input("Маған сұрақ қойып көр (мысалы: Сәлем):")

if st.button("Жауап алу"):
    if prompt:
        with st.spinner("Ойланып жатырмын..."):
            try:
                # Ең жаңа модельді қолдану
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(prompt)
                st.balloons() # Жеңіс белгісі!
                st.success(response.text)
            except Exception as e:
                # Егер flash істемесе, ескірек нұсқасын байқау
                try:
                    model = genai.GenerativeModel('gemini-pro')
                    response = model.generate_content(prompt)
                    st.success(response.text)
                except:
                    st.error("Кішкене күте тұрыңыз, сервер жаңартылып жатыр. 1 минуттан соң бетті жаңартып (refresh) қайта байқаңыз.")
