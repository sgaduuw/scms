from flask import Blueprint

loggedin = Blueprint(
    'loggedin',
    __name__
)

from scms.routes.loggedin import user # noqa
from scms.routes.loggedin import content # noqa
