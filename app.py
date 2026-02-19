import streamlit as st
import asyncio
import edge_tts
import os
import google.generativeai as genai

# ЖИ баптаулары
genai.configure(api_key="AIzaSyBBj0iZFbTuj8cGWGu4Q_iiYG9kzWJIZr0")
genai.configure(api_key="AIzaSyBBj0iZFbTuj8cGWGu4Q_iiYG9kzWJIZr0")
model = genai.GenerativeModel('models/gemini-1.5-flash')
st.set_page_config(page_title="ЖИ Ұстаз", page_icon="🤖")
st.title("🤖 Ақылды Робот-Ұстаз")

user_input = st.text_input("Маған сұрақ қой немесе тақырып бер:", "Абай Құнанбаев кім?")

async def text_to_speech(text):
    VOICE = "kk-KZ-DauletNeural" 
    output_file = "voice.mp3"
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(output_file)
    return output_file

if st.button("Сұрау және Тыңдау"):
    if user_input:
        with st.spinner('Робот ойланып жатыр...'):
            try:
                response = model.generate_content(f"Сен мектеп мұғалімісің. Қазақша қысқа жауап бер: {user_input}")
                answer_text = response.text
                st.info(answer_text)
                
                audio_path = asyncio.run(text_to_speech(answer_text))
                with open(audio_path, "rb") as f:
                    st.audio(f.read(), format="audio/mp3")
            except Exception as e:
                st.error(f"Қате шықты: {e}")