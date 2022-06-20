""" function for index page"""

import random
from datetime import datetime

import lorem
from flask import render_template

from scms import app
from scms.models import Content, Site, m_session


@app.route('/')
def index():
    """ function for displaying the index page """
    # keep adding a page to the site, simply because we can and we eventually
    # will start hitting some scaling stuff.

    # select one random site to insert lorem into
    rnd_site = Site.query.find({'name': random.choice(['test01', 'test02', 'test03'])}).first()
    new_page = Content(
        title=lorem.get_sentence(),
        site_id=rnd_site._id,
        create_date=datetime.now(),
        body=lorem.get_paragraph(
            count=3,
            comma=(0, 2),
            word_range=(4, 8),
            sentence_range=(5, 10)
        )
    )
    m_session.flush()
    return render_template('index.html', payload=new_page, site=rnd_site)