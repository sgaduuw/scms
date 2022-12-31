from flask import render_template
from flask_login import login_required

from scms.extensions import login_manager
from scms.models import User, Site
from scms.routes.admin import admin


@login_manager.user_loader
def load_user(user_id):

    return User.objects(pk=user_id).first()


@admin.route('/admin/sites/')
@login_required
def admin_sites():

    context = {
        'sites': Site.objects
    }

    return render_template('admin_sites.j2', **context)
