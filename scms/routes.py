from scms import app
#from scms import models
from scms.models import session, WikiPage

@app.route('/')
def index():
    wp = WikiPage(title='FirstPage',
                  text='This is a page')
    print(session)
    session.flush()
    return f'Hello World! {wp.title}'
