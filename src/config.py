"""
config.py

This module and class define the environment configuration for the application.
The class reads environment variables and sets default values for the app's configuration.
"""

import os


class Env:
    """
    Environment configuration class.
    """
    GOOGLE_API_KEY: str = os.environ["GOOGLE_API_KEY"]  # The API key for Google services.
    DEBUG: bool = os.environ.get("DEBUG", "False").lower() == "true"  # Debug mode flag.
    LANGUAGE_MODEL: str = os.environ.get("LANGUAGE_MODEL", "gemini-2.0-flash")  # The language model to use.
    HOST: str = os.environ.get("HOST", "0.0.0.0")  # The host address for the app.
    PORT: int = int(os.environ.get("PORT", "8080"))  # The port number for the app.
