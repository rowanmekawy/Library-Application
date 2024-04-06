# from flask import Flask
# from flask_cors import CORS
# from flask_mongoengine import MongoEngine
# from config import config

# app = Flask(__name__)
# CORS(app)

# # Your Flask routes and configuration

# if __name__ == '__main__':
#     app.run(debug=True)

# app.config.from_object(config['development'])
# db = MongoEngine(app)


from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from config import config

app = Flask(__name__)
CORS(app)

# Set the configuration explicitly
app.config.from_object(config['development'])

# Initialize MongoDB
db = MongoEngine(app)

# Your Flask routes and configuration

if __name__ == '__main__':
    app.run(debug=True)
