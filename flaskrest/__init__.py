from flask import Flask
app = Flask(__name__)

import flaskrest.views
from flaskrest.database import db
from flaskrest.database import init_db
from flaskrest.database import destroy_db
init_db()

class AppConfig(object):
  """Application specific configuaration class"""
  def __init__(self, version):
    self.api_version = version;



appconfig  = AppConfig("v0.1")

app.config.from_object('config')

# Flask will automatically remove database sessions at the
# end of the request or when the application shuts down:
@app.teardown_appcontext
def shutdow_session(exception=None):
  db.session.remove()
