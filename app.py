from flask import Flask
from config import config
from flask_graphql import GraphQLView
from schema import schema
from flask_cors import CORS


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config[config_name])
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

    return app
