import typing
from flask import render_template
import lorem
from scms import app
#from scms import models

from scms.models import session, Site, Page

if typing.TYPE_CHECKING:
    from ming.metadata import Manager

@app.route('/')
def index():
    # keep adding a page to the site, simply because we can and we eventually
    # will start hitting some scaling stuff.
    wp = Page(
        dict(
            title='FirstPage',
            text=lorem.get_paragraph(
                count=3,
                comma=(0, 2),
                word_range=(4, 8),
                sentence_range=(5, 10)
            )
        )
    )
    wp.m.save()
    return render_template('index.html', payload=wp)

@app.route('/list')
def list_pages():
    pages = Page.m.find().all()
    return render_template('list.html', pages=pages)
