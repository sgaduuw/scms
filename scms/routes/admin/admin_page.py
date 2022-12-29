from flask import render_template
from flask_login import login_required

from scms.extensions import login_manager
from scms.models import User, Site, Content, Tag, Category
from scms.routes.admin import admin

import lorem


@login_manager.user_loader
def load_user(user_id):

    return User.objects(pk=user_id).first()


@admin.route('/admin/')
@login_required
def admin_page():
    mock_content = {
        'title': lorem.get_word(count=5),
        'body': lorem.get_paragraph(count=7)
    }
    Content(**mock_content).save()

    context = {
        'sites': Site.objects,
        'tags': Tag.objects,
        'categories': Category.objects,
        'posts': Content.objects
    }
    # return f"Front page for {request.headers['Host']}"
    return render_template('admin.j2', **context)
