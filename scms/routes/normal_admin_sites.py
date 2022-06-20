""" admin function for listing sites """

from flask import render_template, session
from scms import app
from scms.models import Site


@app.route('/admin/sites', strict_slashes=False)
def normal_admin_sites():
    """ list sites """
    try:
        session['admin_logged_in']

    except KeyError:
        return render_template('admin_normal_list_sites.html', active_admin=False), 401

    else:
        sites = Site.query.find()

        return render_template('admin_normal_list_sites.html', active_admin=True, sites=sites)
