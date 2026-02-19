import streamlit as st
import google.generativeai as genai

# МЫНА ЖЕРГЕ ӨЗ КІЛТІҢДІ ТЫРНАҚШАНЫҢ ІШІНЕ ҚОЙ
genai.configure(api_key="АЛҒАН_API_КІЛТІҢДІ_ОСЫНДА_ЖАЗ")

st.title("🤖 Ақылды Робот-Ұстаз")
model = genai.GenerativeModel('gemini-1.5-flash')

prompt = st.text_input("Маған сұрақ қой:")
if st.button("Жауап ал"):
    try:
        response = model.generate_content(prompt)
        st.write(response.text)
    except Exception as e:
        st.error(f"Қате: {e}")
