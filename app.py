import streamlit as st
import google.generativeai as genai

# МЫНА ЖЕРГЕ ӨЗ КІЛТІҢДІ ТЫРНАҚШАНЫҢ ІШІНЕ ҚОЙ
# Скриншоттағы AIzaSy... деп басталатын кілтті жаз
genai.configure(api_key="AIzaSy...ОСЫ_ЖЕРГЕ_ӨЗ_КІЛТІҢДІ_ЖАЗ")

st.set_page_config(page_title="ЖИ Ұстаз", page_icon="🤖")
st.title("🤖 Ақылды Робот-Ұстаз")
st.write("Сұрағыңызды төменге жазыңыз:")

model = genai.GenerativeModel('gemini-1.5-flash')

prompt = st.text_input("Сұрақ:", placeholder="Абай Құнанбаев кім?")

if st.button("Жауап ал"):
    if prompt:
        try:
            response = model.generate_content(prompt)
            st.success(response.text)
        except Exception as e:
            st.error(f"Қате шықты: {e}")
    else:
        st.warning("Алдымен сұрақ жазыңыз!")
