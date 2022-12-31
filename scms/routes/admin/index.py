from flask import render_template
from flask_login import login_required

from scms.extensions import login_manager
from scms.models import User, Site, Content, Tag, Category
from scms.routes.admin import admin

import lorem
import random


@login_manager.user_loader
def load_user(user_id):

    return User.objects(pk=user_id).first()


@admin.route('/admin/')
@login_required
def index():
    site_names = ['Local Eelco', 'Eelco02', 'Eelco03']
    author_names = ['aa', 'bb', 'cc']

    random_site = random.choice(site_names)
    random_author = random.choice(author_names)
    site = Site.objects(name=random_site).first()
    user = User.objects(user_name=random_author).first()

    mock_content = {
        'site': site.id,
        'author': user.id,
        'title': lorem.get_word(count=5),
        'body': lorem.get_paragraph(count=7)
    }
    Content(**mock_content).save()

    context = {
        'sites': Site.objects,
        'authors': User.objects,
        'content': Content.objects,
        'tags': Tag.objects,
        'categories': Category.objects,
        'posts': Content.objects
    }
    # return f"Front page for {request.headers['Host']}"
    return render_template('admin_index.j2', **context)
