import streamlit as st
import google.generativeai as genai

# API кілтің
genai.configure(api_key="AIzaSyBBj0iZFbTuj8cGWGu4Q_iiYG9kzWJIZr0")

st.set_page_config(page_title="Ақылды Чат-бот", page_icon="💬")
st.title("💬 Нағыз Чат-бот")

# Есте сақтау (History) бөлімі
if "messages" not in st.session_state:
    st.session_state.messages = []

# Ескі жазысқан хаттарды экранға шығару
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Модельді баптау
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

# Сұрақ жазатын жол (Чат стилінде)
if prompt := st.chat_input("Хабарлама жазыңыз..."):
    # Пайдаланушы хабарламасын көрсету
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Роботтың жауабы
    with st.chat_message("assistant"):
        try:
            response = chat.send_message(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Қате: {e}")
