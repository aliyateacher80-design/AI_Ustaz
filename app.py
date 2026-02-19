import streamlit as st
import google.generativeai as genai

# API кілтің (Кілтті осы жерде қалдырдым)
genai.configure(api_key="AIzaSyBBj0iZFbTuj8cGWGu4Q_iiYG9kzWJIZr0")

st.set_page_config(page_title="AI Ұстаз", page_icon="🤖")
st.title("🤖 Менің Ақылды Роботым")

# Сұрақ жазатын орын
prompt = st.text_input("Маған сұрақ қойыңыз:")

if st.button("Жауап алу"):
    if prompt:
        with st.spinner("Ойланып жатырмын..."):
            try:
                # ЕҢ ҚАРАПАЙЫМ ЖОЛ
                model = genai.GenerativeModel('gemini-pro')
                response = model.generate_content(prompt)
                
                st.write("---")
                st.success(response.text)
                st.balloons() # Жеңіс шарлары!
            except Exception as e:
                # Егер тағы қате шықса, себебін анық көрсетеді
                st.error(f"Қате шықты: {e}")
                st.info("GitHub-та 'requirements.txt' файлын жасау керек болуы мүмкін.")

