from flask import Flask
from app.routes import ChatController

app: Flask = Flask(__name__)
ChatController(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
