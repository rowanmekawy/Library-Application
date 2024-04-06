from flask import jsonify
from flask_restful import Api, Resource
from . import api_bp

api = Api(api_bp)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')