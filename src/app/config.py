import os

class Env:
    GOOGLE_API_KEY: str = os.environ["GOOGLE_API_KEY"]
    DEBUG: bool = os.environ.get("DEBUG", "False").lower() == "true"
    LANGUAGE_MODEL: str = os.environ.get("LANGUAGE_MODEL", "gemini-2.0-flash")
