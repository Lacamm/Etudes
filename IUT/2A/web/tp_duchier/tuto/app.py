from flask import Flask
app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
from flask_bootstrap import Bootstrap

Bootstrap(app)

import os.path
def mkpath(p):
    return os.path.normpath(
        os.path.join(
            os.path.dirname(__file__),
        p))


from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'sqlite:///'+mkpath('../myapp.db'))

app.config['SECRET_KEY'] = "d3f5b563-9b4c-4c47-871e-adfe452a4e5f"

db = SQLAlchemy(app)
    

from flask_login import LoginManager
login_manager = LoginManager(app)