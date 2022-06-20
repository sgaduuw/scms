""" function for listing pages """

from urllib.parse import urlparse

from flask import render_template, request
from scms import app
from scms.models import Site


@app.route('/list')
def list_pages():
    """ function for listing all pages on all sites """

    req_host = urlparse(request.base_url).hostname
    site = Site.query.find({"fqdns": req_host }).first()

    if site is not None:
        return render_template('list.html', site=site)

    return render_template('error.html', payload=req_host), 404
