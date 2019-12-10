from flask import Flask
from .extensions import db
from .api import api
from .commands import create_tables


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    app.cli.add_command(create_tables)
    db.init_app(app)
    app.register_blueprint(api)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
