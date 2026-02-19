import streamlit as st
import google.generativeai as genai

# МЫНА ЖЕРГЕ ӨЗ КІЛТІҢДІ ТЫРНАҚШАНЫҢ ІШІНЕ ҚОЙ
genai.configure(api_key="ОСЫ_ЖЕРГЕ_ӨЗ_КІЛТІҢДІ_ЖАЗ")

st.title("🤖 Ақылды Робот-Ұстаз")
st.write("Сұрақ қойыңыз, мен сізге жауап беремін!")

model = genai.GenerativeModel('gemini-1.5-flash')

prompt = st.text_input("Сұрағыңызды жазыңыз:")

if st.button("Жауап алу"):
    if prompt:
        try:
            response = model.generate_content(prompt)
            st.success(response.text)
        except Exception as e:
            st.error(f"Қате шықты: {e}")
    else:
        st.warning("Алдымен сұрақ жазыңыз!")
