from flask_restplus import Resource, Namespace, fields
from flask import jsonify
from flask import request, Response
from flask import current_app as app

api = Namespace('information', description='Information APIs')
g_parser = api.parser()


@api.route('')
@api.expect(g_parser)
@api.response(401, 'Authentication failed')
@api.response(422, 'Error occured, see response body for details')

class Index(Resource):
    info_model = api.model('info',{})
    @api.response(200, 'Success', model=info_model)
    def get(self, **kwargs):
        message = {
            "title": "API BASE",
            "version": "v1.0",
            "author": "Chung Phan",
            "email": "chungphan7819@gmail.com",
            "message": "api base"
        }
        return jsonify(message)
