import streamlit as st
import google.generativeai as genai

# API КІЛТІҢ
genai.configure(api_key="AIzaSyBBj0iZFbTuj8cGWGu4Q_iiYG9kzWJIZr0")

st.set_page_config(page_title="AI Ұстаз", page_icon="🤖")
st.title("🤖 Менің Ақылды Роботым")

prompt = st.text_input("Маған сұрақ қойыңыз:")

if st.button("Жауап алу"):
    if prompt:
        with st.spinner("Ойланып жатырмын..."):
            try:
                # МӘЖБҮРЛІ ТҮРДЕ v1 НҰСҚАСЫН ЖӘНЕ flash МОДЕЛІН ҚОЛДАНУ
                # Бұл 404 қатесін болдырмаудың ең сенімді жолы
                model = genai.GenerativeModel(
                    model_name='gemini-1.5-flash'
                )
                
                response = model.generate_content(prompt)
                
                st.write("---")
                if response.text:
                    st.success(response.text)
                    st.balloons() # Жеңіс шарлары!
                else:
                    st.warning("Жауап бос келді. Қайта байқаңыз.")
                    
            except Exception as e:
                # Егер тағы да 404 шықса, серверді "ояту" үшін хабарлама
                st.error(f"Қате: {e}")
                st.info("Сервер жаңартылуда. Егер қате кетпесе, Streamlit Cloud-та 'Reboot App' жасаңыз.")
