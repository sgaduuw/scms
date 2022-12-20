from flask import Blueprint
from scms.extensions import login_manager

from scms.models import User

admin = Blueprint(
    'admin',
    __name__
)


@login_manager.user_loader
def load_user(user_id):

    return User.objects(pk=user_id).first()

from scms.routes.admin import admin_page # noqa
