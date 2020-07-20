from flask import Blueprint
from flask_restful import Resource, Api


properties_blueprint = Blueprint('properties', __name__)
api = Api(properties_blueprint)


class PropertiesPing(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!',
            'service' : 'properties'
        }


api.add_resource(PropertiesPing, '/properties/ping')