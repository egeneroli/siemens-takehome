# src/app/controllers/chat_controller.py

from flask import Blueprint, request, jsonify, Flask
from typing import Any
from chat.service import ChatService


class ChatController:
    """
    A class-based controller for the chat endpoint.
    Wraps a Blueprint to attach endpoints OOP style.
    """

    def __init__(self, app: Flask) -> None:
        # Create a ChatService instance
        self.chat_service: ChatService = ChatService()

        # Create a Blueprint and register routes
        self.bp: Blueprint = Blueprint("chat", __name__)
        self.bp.add_url_rule("/", view_func=self.home, methods=["GET"])
        self.bp.add_url_rule("/chat", view_func=self.chat, methods=["POST"])
        app.register_blueprint(self.bp)

    def home(self) -> tuple[str, int]:
        """
        GET /
        Returns a welcome message for the chatbot.
        """
        return "Welcome to the Chatbot", 200

    def chat(self) -> tuple[dict, int]:
        """
        POST /chat
        Accepts JSON with 'prompt' key and returns a JSON response from the LLM.
        """
        PROMPT_KEY: str = "prompt"
        data: dict[str, Any] = request.get_json()
        if not data or PROMPT_KEY not in data:
            return jsonify({"error": f"Please provide '{PROMPT_KEY}' in the request body."}), 400

        user_prompt: str = data[PROMPT_KEY]
        response_text: str = self.chat_service.get_reply(user_prompt)
        return jsonify({"response": response_text}), 200
