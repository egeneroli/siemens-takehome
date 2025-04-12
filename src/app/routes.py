from flask import Blueprint, request, jsonify
from langchain_integration.chat_service import ChatService

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = ChatService.get_response(user_input)
    return jsonify({'response': response})
