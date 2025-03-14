from flask import Flask
import os.path
from flask_bootstrap import Bootstrap

app = Flask(__name__)

Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

def mkpath(p):
    """
     renvoie repertoire courant
    """
    return os.path.normpath(
        os.path.join(
            os.path.dirname(file),
            p))


