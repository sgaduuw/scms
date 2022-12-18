from flask import Blueprint

public = Blueprint(
    'public',
    __name__
)

from scms.routes.public import index # noqa
