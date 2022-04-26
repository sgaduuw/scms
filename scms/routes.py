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
    wp = WikiPage(title='FirstPage',
                  text='This is a page')
    print(session)
    session.flush()
    return f'Hello World! {wp.title}'
