from flask import Flask

from scms.config import Config
from scms.routes.public import public
from scms.routes.auth import auth
from scms.routes.admin import admin


from scms.extensions import (
    bcrypt,
    cache,
    csrf_protect,
    db,
    debug_toolbar,
    flask_static_digest,
    login_manager
)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    csrf_protect.init_app(app)
    login_manager.init_app(app)
    flask_static_digest.init_app(app)
    debug_toolbar.init_app(app)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(public)
    app.register_blueprint(auth)
    app.register_blueprint(admin)
    return None


if __name__ == 'main':
    app = create_app()
    app.run()
