from flask import Flask

app = Flask(__name__)
app.config.from_prefixed_env()

# import scms.views
from scms import routes

if __name__ == 'main':
    app.run()
