import os
from common.config import config
from flask import Flask, request, g, abort, session
from flask_restplus import Api, Resource, Namespace
from flask import Flask, Blueprint
from flask import current_app as app

ENV = os.environ.get('ENV', 'development')
CONF = config[ENV]


def create_app():
    app = Flask(__name__)
    env = os.environ.get('ENV', 'development')
    return app
