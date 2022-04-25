from flask import Flask
app = Flask(__name__)

# import scms.views
from scms import routes

if __name__ == 'main':
    app.run()
