import streamlit as st
from chat.service import ChatService

# Initialize ChatService once
chat_service: ChatService = ChatService()

# Header
st.title('Chat with AI')

# Get user input
user_input: str = st.text_input('You:')

# Get AI response if button is clicked
if st.button('Send'):
    response: str = chat_service.get_reply(user_input)
    st.write('AI:', response)
