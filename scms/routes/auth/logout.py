from flask import (
    redirect,
    url_for
)
from flask_login import logout_user, login_required

from scms.extensions import login_manager
from scms.routes.auth import auth
from scms.models import User


@login_manager.user_loader
def load_user(user_id):

    return User.objects(pk=user_id).first()


@auth.route('/logout/', methods=["GET", "POST"])
@login_required
def logout():
    logout_user()

    return redirect(url_for("public.index"))
