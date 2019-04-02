from flask_restplus import Api, Namespace
from flask import Blueprint
import os
from common.config import config
from flask import current_app as app
from api import create_app

from api.index import api as index_namespace
from api.happy import api as happy_namespace


ENV = os.environ.get('ENV', 'development')
CONF = config[ENV]

blueprint = Blueprint('api', __name__)

api = Api(blueprint, doc='/doc/')

api.add_namespace(index_namespace, path='/')
api.add_namespace(happy_namespace, path='/resource')

app = create_app()
app.register_blueprint(blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999, debug=True)
