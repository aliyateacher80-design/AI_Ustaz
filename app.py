import streamlit as st
import google.generativeai as genai
import edge_tts
import asyncio
import os

# СЕНІҢ API КІЛТІҢ (Осы жерді тексер)
genai.configure(api_key="AIzaSyBBj0iZFbTuj8cGWGu4Q_iiYG9kzWJIZr0")

st.title("🤖 Ақылды Робот-Ұстаз")

# Моделді ең сенімді нұсқаға ауыстырдық
model = genai.GenerativeModel('gemini-pro')

prompt = st.text_input("Маған сұрақ қой немесе тақырып бер:", "Абай Құнанбаев кім?")

if st.button("Сұрау және Тыңдау"):
    try:
        # 1. Жауап алу
        response = model.generate_content(prompt)
        text_reply = response.text
        st.write(text_reply)
        
        # 2. Дауысқа айналдыру
        async def speak(text):
            communicate = edge_tts.Communicate(text, "kk-KZ-AigulNeural")
            await communicate.save("output.mp3")
        
        asyncio.run(speak(text_reply))
        
        # 3. Аудионы шығару
        st.audio("output.mp3")
        
    except Exception as e:
        st.error(f"Қате шықты: {e}")


