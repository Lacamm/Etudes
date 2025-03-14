from .app import app, db
from flask import render_template, url_for, redirect
from .models import get_sample, get_author, Author, User
from flask_wtf import  FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import  DataRequired


import yaml, os.path


@app.route("/save/author/", methods=("POST",))
def save_author():
        a = None
        f = AuthorForm()
        if f.validate_on_submit():
                id =int (F.id.data)
                a = get_author(id)
                a.name = f.name.datadb.session.commit()
                return redirect(url_for('one_author', id=a.id))
        a = get_author(int(f.id.data))
        return render_template("edit-author.html", author=a, form=f)

class AuthorForm(FlaskForm):
        id= HiddenField('id')
        name = StringField('Nom', validators=[DataRequired()])

@app.route("/edit/author/<int:id>")
def edit_author(id):
        a = get_author(id)
        f = AuthorForm(id=a.id, name=a.name)
        return render_template("edit-author.html", author=a, form=f)



@app.route("/")
def home():
    return render_template(
        "home.html",
        title="Tiny Amazon",
        books=get_sample())
    

@app.route("/page2")
def page2():
    return render_template(
        "page2.html",
        title="Page 2",
    )