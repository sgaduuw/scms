from flask import render_template
from flask_login import login_required, current_user

from scms.extensions import login_manager
from scms.helpers import Header
from scms.models import User, Site
from scms.routes.loggedin import loggedin


@login_manager.user_loader
def load_user(user_id):

    return User.objects(pk=user_id).first()


@loggedin.route('/u/edit/')
@login_required
def edit_content():

    header = Header(
        url_text=current_user.first_name
    )
    # header = Header()

    context = {
        'header': header,
        'user': current_user
    }

    return render_template('content_edit.j2', **context)
