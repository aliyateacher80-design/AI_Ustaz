import streamlit as st
import google.generativeai as genai

# API кілтің
genai.configure(api_key="AIzaSyBBj0iZFbTuj8cGWGu4Q_iiYG9kzWJIZr0")

st.set_page_config(page_title="AI Ұстаз", page_icon="🤖")
st.title("🤖 Менің Ақылды Роботым")

prompt = st.text_input("Маған сұрақ қойыңыз:")

if st.button("Жауап алу"):
    if prompt:
        with st.spinner("Ойланып жатырмын..."):
            try:
                # МОДЕЛЬДІҢ ЕҢ ТҰРАҚТЫ АТЫН ҚОЛДАНАМЫЗ
                model = genai.GenerativeModel(model_name='gemini-1.5-flash-latest')
                
                # Жауап алу
                response = model.generate_content(prompt)
                
                st.write("---")
                if response.text:
                    st.success(response.text)
                    st.balloons()
                else:
                    st.warning("Жауап бос келді. Қайта байқап көріңіз.")
                    
            except Exception as e:
                # Егер тағы қате шықса, оны анық көрсетеді
                st.error(f"Қате: {e}")
                st.info("Кеңес: API кілтіңіздің жұмыс істеп тұрғанын тексеріңіз.")
