""" Module for Server configuration """

from flask import Flask
from config.environment import AppConfig
from api.controller.user import User
from db import connectMilvus
from flask_restful import Api

def create_app(config=AppConfig):
    """ Create the flask application """
    app = Flask(__name__, template_folder='../templates')
    app.config.from_object(config)

    api = Api()
    api.init_app(app)
    api.add_resource(User, "/user")
    
    connectMilvus()

    return app


application = create_app()