"""
routes.py

This module defines the routes for the chat application.
It contains the ChatController class, which manages the chat endpoints,
including the home and chat routes for handling user interactions.
"""

from flask import Blueprint, request, jsonify, Flask, Response
from typing import Any
from chat.chat_service import ChatService


class ChatController:
    """
    A class-based controller for the chat endpoint.
    Wraps a Blueprint to attach endpoints OOP style.
    """

    def __init__(self, app: Flask) -> None:
        """
        Initialize the ChatController with a Flask app.

        Parameters
        ----------
        app : Flask
            The Flask application instance to register the blueprint with.
        """
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

        Returns: tuple[str, int]
            A tuple containing the welcome message and HTTP status code.
        """
        return "Welcome to the Chatbot", 200

    def chat(self) -> tuple[Response, int]:
        """
        POST /chat
        Accepts JSON with 'prompt' key and returns a JSON response from the LLM.

        Returns: tuple[Response, int]
            A tuple containing the JSON response and HTTP status code.
        """
        PROMPT_KEY: str = "prompt"
        try:
            # Parse JSON request data
            data: dict[str, Any] = request.get_json()
            if not data or PROMPT_KEY not in data:
                return jsonify({"error": f"Please provide '{PROMPT_KEY}' in the request body."}), 400

            # Get user prompt from request data
            user_prompt: str = data[PROMPT_KEY]
            # Get response from chat service
            response_text: str = self.chat_service.get_reply(user_prompt)
            return jsonify({"response": response_text}), 200

        except Exception as e:
            # Return error response
            return jsonify({"error": str(e)}), 500
