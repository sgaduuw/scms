""" routes for scms app """
import datetime
import random
from urllib.parse import urlparse

import lorem
from flask import render_template, request

from scms import app
from scms.models import Page, Site, session


@app.route('/')
def index():
    """ function for displaying the index page """
    # keep adding a page to the site, simply because we can and we eventually
    # will start hitting some scaling stuff.

    # select one random site to insert lorem into
    rnd_site = Site.query.find({'name': random.choice(['test01', 'test02', 'test03'])}).first()
    new_page = Page(
        title='FirstPage',
        site_id=rnd_site._id,
        date=datetime.datetime.now(),
        text=lorem.get_paragraph(
            count=3,
            comma=(0, 2),
            word_range=(4, 8),
            sentence_range=(5, 10)
        )
    )
    session.flush()
    return render_template('index.html', payload=new_page)

@app.route('/list')
def list_pages():
    """ function for listing all pages on all sites """

    req_host = urlparse(request.base_url).hostname
    site = Site.query.find({"fqdns": req_host }).first()

    if site is not None:
        print(req_host)
        return render_template('list.html', site=site)

    return render_template('error.html', payload=req_host), 404
