"""
main.py

This module initializes and runs the Flask application.
It sets up the configuration, registers routes, and starts the server.
"""

from flask import Flask
from chat_controller import ChatController
from config import Env

# create the Flask app
app: Flask = Flask(__name__)

# configure the app
app.config.from_object(Env)

# register the routes
ChatController(app)

# run the app
if __name__ == '__main__':
    app.run(host=Env.HOST, port=Env.PORT, debug=Env.DEBUG)
