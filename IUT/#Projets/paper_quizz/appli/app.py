from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os.path

app = Flask(__name__)

# /* BOOTSTRAP */
Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

def mkpath(p):
    return os.path.normpath(
        os.path.join(
            os.path.dirname(__file__), p
        )
    )
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///"+mkpath("../paper_quizz.db")
)
db = SQLAlchemy(app)

app.config["SECRET_KEY"] = "cee66fd4-60e0-4ff0-96f5-8102964e87c0"
login_manager = LoginManager(app)