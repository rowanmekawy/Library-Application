from app import create_app
from config import Config
from flask import Flask
from flask_cors import CORS

app = create_app(Config)
CORS(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

