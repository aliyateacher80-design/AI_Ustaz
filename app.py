import streamlit as st
import google.generativeai as genai

# API кілтің
genai.configure(api_key="AIzaSyBBj0iZFbTuj8cGWGu4Q_iiYG9kzWJIZr0")

st.set_page_config(page_title="AI Ұстаз", page_icon="🤖")
st.title("🤖 Менің Ақылды Роботым")

# Сұрақ жазатын орын
prompt = st.text_input("Маған сұрақ қойыңыз:")

if st.button("Жауап алу"):
    if prompt:
        with st.spinner("Ойланып жатырмын..."):
            try:
                # ЕҢ ТҰРАҚТЫ МОДЕЛЬ АТЫ (v1beta-сыз жұмыс істейді)
                model = genai.GenerativeModel('gemini-1.5-flash-001')
                
                # Жауапты алу
                response = model.generate_content(prompt)
                
                st.write("---")
                if response.text:
                    st.success(response.text)
                    st.balloons() # Мерекелік шарлар!
            except Exception as e:
                # Егер тағы да 404 шықса, соңғы амал:
                try:
                    model = genai.GenerativeModel('gemini-1.0-pro')
                    response = model.generate_content(prompt)
                    st.success(response.text)
                except:
                    st.error(f"Қате: {e}")
                    st.info("Бұл Google серверіндегі уақытша техникалық мәселе болуы мүмкін. 5 минуттан соң қайталап көріңіз.")
