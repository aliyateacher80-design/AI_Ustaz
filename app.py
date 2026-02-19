import streamlit as st
import google.generativeai as genai

# Сенің API кілтің
genai.configure(api_key="AIzaSyBBj0iZFbTuj8cGWGu4Q_iiYG9kzWJIZr0")

st.set_page_config(page_title="Ақылды Робот-Ұстаз", page_icon="🤖")

st.title("🤖 Ақылды Робот-Ұстаз")
st.write("Сұрағыңызды жазыңыз, мен жауап беремін!")

# Модельді баптау
model = genai.GenerativeModel('gemini-1.5-flash')

prompt = st.text_input("Сұрақ:", placeholder="Абай Құнанбаев кім?")

if st.button("Жауап ал"):
    if prompt:
        with st.spinner('Ойланып жатырмын...'):
            try:
                response = model.generate_content(prompt)
                st.success("Жауап:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Қате шықты: {e}")
    else:
        st.warning("Алдымен сұрақ жазыңыз!")
