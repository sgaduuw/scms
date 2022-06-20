""" admin functions for normal login """

from flask import redirect, render_template, session, url_for
from scms import app
from scms.login_forms import AdminLoginForm
from scms.models import User


@app.route('/admin/login', methods=['GET', 'POST'], strict_slashes=False)
def normal_admin_login():
    """ function for logging in to the normal admin page """
    

    form = AdminLoginForm()

    if form.validate_on_submit():
        if form.username.data:
            user = User.query.find({ 'username': form.username.data }).first()
            print(f"user: {user}")
            validate = user.validate_password(form.password.data)
            print(f"validate: {validate}")
            if validate:
                session['admin_logged_in'] = True
                return redirect(url_for('normal_admin'))

    return render_template('admin_login.html', form=form)
