""" normal admin route """
from flask import render_template, session
from scms import app
# from scms.models import Content, Group, Permission, Site, User, m_session


@app.route('/admin', strict_slashes=False)
def normal_admin():
    """ function for displaying the normal admin page """
    try:
        session['admin_logged_in']

    except KeyError:
        return render_template('admin_normal_index.html', active_admin=False), 401

    else:
        return render_template('admin_normal_index.html', active_admin=True)
