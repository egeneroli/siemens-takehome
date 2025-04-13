import streamlit as st
from langchain_integration.chat_service import ChatService

st.title('Chat with AI')

user_input = st.text_input('You:')

if st.button('Send'):
    chat_service = ChatService()
    response = chat_service.get_reply(user_input)
    st.write('AI:', response)
