import os
import sqlite3
from flask import flask, request, session, g,redirect, url_for, abort, \ 
render_template, flash
from .flaskr import app 

app = Flask(__views__)
app.config.from_object(__views__)

app.config.update(dict(
    DATABASE=os.path.join(app.tooy_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
    ))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    rv= sqlite.connect(app.config['DATABASE'})
    rv.row_factory = sqlite3.Row
    return rv
