import os
import openai
import streamlit as st

# Устанавливаем ключ OpenAI из секретов
openai.api_key = st.secrets['OPENAI_API_KEY']

st.set_page_config(page_title="Simple Chatbot")
st.title("Chatbot Example")

# Инициализируем список сообщений в сессии
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Функция для вывода сообщений на экран
def display_messages():
    for msg in st.session_state["messages"]:
        st.write(f"{msg['role'].capitalize()}: {msg['content']}")

# Выводим предыдущие сообщения
display_messages()

# Ввод сообщения от пользователя
user_input = st.text_input("Введите сообщение:")

# Если пользователь ввел сообщение
if user_input:
    # Добавляем сообщение пользователя в список
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Отправляем запрос к OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state["messages"],
    )

    # Получаем ответ от модели
    assistant_reply = response['choices'][0]['message']['content']

    # Добавляем ответ ассистента в сообщения
    st.session_state["messages"].append({"role": "assistant", "content": assistant_reply})

    # Обновляем страницу для отображения новых сообщений
    st.experimental_rerun()

# Выводим новый диалог после ответа ассистента
display_messages()
