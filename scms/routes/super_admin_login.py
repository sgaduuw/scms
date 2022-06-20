""" super admin functions for login """

import os

from flask import redirect, render_template, session, url_for
from scms import app
from scms.login_forms import SALoginForm
from scms.models import User


@app.route('/SA/login', methods=['GET', 'POST'], strict_slashes=False)
def super_admin_login():
    """ function for logging in to the superadmin page """
    if User.query.find().count() == 0:
        form = SALoginForm()
        if os.getenv('SUPERADMIN_PASSWORD') is None:
            raise Exception('SUPERADMIN_PASSWORD environment variable not set')

        if form.validate_on_submit():
            if form.password.data == os.getenv('SUPERADMIN_PASSWORD'):
                session['sa_logged_in'] = True
                return redirect(url_for('super_admin'))

        return render_template('admin_super_login.html', form=form)

    return render_template('error.html'), 401
