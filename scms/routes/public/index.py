from flask import render_template

from scms.routes.public import public


@public.route('/')
def index():

    return render_template('index.html')
