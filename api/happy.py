from flask_restplus import Resource, Namespace, fields
from flask import jsonify
from flask import request, Response
from flask import current_app as app
import random

api = Namespace('resouces', description='resouces APIs')
g_parser = api.parser()

TEST_FUNC = ["loesm isum mens", "onsectetur adipiscing elit", " sed do eiusmod tempor incididunt", "Ut enim ad minim veniam", "Lorem ipsum dolor sit amet", "T Duis aute irure dolor"]


@api.route('')
@api.expect(g_parser)
@api.response(401, 'Authentication failed')
@api.response(422, 'Error occured, see response body for details')

class Happy(Resource):
    info_model = api.model('info',{})
    @api.response(200, 'Success', model=info_model)
    def get(self, **kwargs):
        message = {
            "output": random.choice(TEST_FUNC)
        }
        return jsonify(message)