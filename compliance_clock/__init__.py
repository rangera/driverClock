import os

from flask import Flask

from .endpoints import (
    EVENT_BP,
    CLOCK_BP,
    )

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'compliance_clock.sqlite'),
    )

    if test_config is None:
        app.config.from_mapping(
        )
    else:
        app.config.from_mapping(test_config)


    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(EVENT_BP)
    app.register_blueprint(CLOCK_BP)


    from . import db
    db.init_app(app)

    return app