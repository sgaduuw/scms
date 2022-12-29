from flask import render_template

from scms.models import Content
from scms.routes.public import public


@public.route('/')
def index():

    list_content = Content.objects

    context = {
        'list_content': list_content
    }

    return render_template('index.j2', **context)
