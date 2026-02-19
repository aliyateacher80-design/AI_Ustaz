import streamlit as st
import google.generativeai as genai

# ӨЗ КІЛТІҢДІ ТЫРНАҚШАНЫҢ ІШІНЕ ҚОЙ
genai.configure(api_key="AIzaSy...ОСЫ_ЖЕРГЕ_ӨЗ_КІЛТІҢДІ_ЖАЗ")

st.title("🤖 Ақылды Робот-Ұстаз")
model = genai.GenerativeModel('gemini-1.5-flash')

prompt = st.text_input("Маған сұрақ қой немесе тақырып бер:", placeholder="Абай Құнанбаев кім?")

if st.button("Жауап ал"):
    if prompt:
        try:
            response = model.generate_content(prompt)
            st.success(response.text)
        except Exception as e:
            st.error(f"Қате шықты: {e}")
    else:
        st.warning("Алдымен сұрақ жазшы!")
