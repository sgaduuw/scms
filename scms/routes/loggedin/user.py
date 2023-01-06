from flask import render_template
from flask_login import login_required

from scms.extensions import login_manager
from scms.helpers import Header
from scms.models import User, Site
from scms.routes.loggedin import loggedin


@login_manager.user_loader
def load_user(user_id):

    return User.objects(pk=user_id).first()


@loggedin.route('/u/<string:user_name>/<string:user_id>/')
@login_required
def page(user_name, user_id):
    user = User.objects(id=user_id, user_name=user_name).first()

    header = Header(
        url_text=user.first_name
    )
    # header = Header()

    context = {
        'header': header,
        'user': user
    }

    return render_template('user.j2', **context)
