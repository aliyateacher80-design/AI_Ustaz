import os
import subprocess
import sys

# СИҚЫРЛЫ ЖОЛ: Кітапхананы сайт ашылғанда өзі орнатады
try:
    import google.generativeai as genai
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google-generativeai"])
    import google.generativeai as genai

import streamlit as st

# Сенің API кілтің
genai.configure(api_key="AIzaSyBBj0iZFbTuj8cGWGu4Q_iiYG9kzWJIZr0")

st.set_page_config(page_title="Ақылды Чат-бот", page_icon="💬")
st.title("💬 Нағыз Чат-бот")

# Есте сақтау бөлімі
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Ең тұрақты модель
model = genai.GenerativeModel('gemini-pro')

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if prompt := st.chat_input("Сұрақ жазыңыз..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = st.session_state.chat.send_message(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("Кішкене күте тұрыңыз, жүйе дайындалып жатыр...")
