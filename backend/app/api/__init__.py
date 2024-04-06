from flask import Blueprint
from flask_restx import Api
from ..exceptions import DatabaseOperationError, InvalidInputError
api_bp = Blueprint('api', __name__)
api = Api(title='My API', version='1.0', description='A simple API')


@api.errorhandler(InvalidInputError)
def handle_invalid_input(error):
    return {'message': str(error)}, 400

@api.errorhandler(DatabaseOperationError)
def handle_database_operation_error(error):
    return {'message': str(error)}, 500