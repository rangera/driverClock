# import os

from flask import Flask

from .endpoints import (
    EVENT_BP,
    CLOCK_BP,
    )

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping()

    app.register_blueprint(EVENT_BP)
    app.register_blueprint(CLOCK_BP)



    return app