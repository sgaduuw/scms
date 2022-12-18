from flask import Blueprint

auth = Blueprint(
    'auth',
    __name__
)

from scms.routes.auth import login # noqa
from scms.routes.auth import logout # noqa
from scms.routes.auth import register # noqa
from scms.routes.auth import forms # noqa
