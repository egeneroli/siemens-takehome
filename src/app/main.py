from flask import Flask
from app.routes import ChatController
from app.config import Env

# create the Flask app
app: Flask = Flask(__name__)

# configure the app
app.config.from_object(Env)

# register the routes
ChatController(app)

# run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
