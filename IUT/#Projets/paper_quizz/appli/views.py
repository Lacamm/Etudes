from .app import app
from .models import *
from flask import render_template, url_for, redirect

from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, PasswordField, SubmitField, validators
from flask_login import login_user, current_user, logout_user

@app.route("/")
def home():
    return render_template(
        "home.html",
        title="Paper Quizz",
    )

class LoginForm(FlaskForm):
    username = StringField("Identifiant")
    password = PasswordField("Mot de Passe")
    submit = SubmitField("Se connecter")

    def get_authenticated_user(self):
        user = get_utilisateurByIdentifiant(self.username.data)
        if user is None:
            return None
        m = sha256()
        m.update(self.password.data.encode())
        password = m.hexdigest()
        return user if password == user.mdp else None

class SignupForm(FlaskForm):
    identifiant = StringField("Identifiant", validators=[validators.DataRequired()])
    prenom = StringField("Prénom", validators=[validators.DataRequired()])
    nom = StringField("Nom", validators=[validators.DataRequired()])
    email = StringField("Adresse mail", 
            validators=[validators.DataRequired(), validators.Email(message='Veuillez entrer une adresse mail valide')])
    email_confirm = StringField("Confirmation de l'adresse mail", 
            validators=[validators.DataRequired(), validators.EqualTo('email', message='Les adresses mail sont différentes')])
    mdp = PasswordField("Mot de passe", validators=[validators.DataRequired()])
    mdp_confirm = PasswordField("Confirmation du mot de passe", 
            validators=[validators.DataRequired(), validators.EqualTo('mdp', message='Les mots de passes sont différents')])
    submit = SubmitField("S'inscrire")
    
    def add_user(self):
        user = add_user(
            identifiant = self.identifiant.data,
            nom = self.nom.data,
            prenom = self.prenom.data,
            email = self.email.data,
            mdp = self.mdp.data
        )
        return user

@app.route("/login", methods=("GET", "POST"))
def login():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('home'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = login_form.get_authenticated_user()
        if user:
            login_user(user)
            return redirect(url_for("home"))
    signup_form = SignupForm()
    if signup_form.validate_on_submit():
        user = signup_form.add_user()
        if user:
            login_user(user)
            return redirect(url_for("home"))
    return render_template(
        "login.html", 
        title = "Connexion",
        login_form = login_form,
        signup_form = signup_form
    )

@app.route("/logout")
def logout():
    return redirect(url_for('login'))

@app.route("/listeQuiz")
def listeQuiz():
    return render_template(
        "listeQuiz.html",
        title = "Liste des Quiz",
        allQuiz = get_allQuiz()
    )


@app.route("/quiz/creer")
def creerQuiz():
    return render_template(
        "creerQuiz.html",
        title="Créer un quiz",
    )

@app.route("/quiz/<int:quiz_id>")
def quiz(quiz_id):
    return render_template(
        "quiz.html",
        title=Quiz.query.get(quiz_id).nom,
    )

@app.route("/quiz/<int:quiz_id>/edit/")
def editerQuiz(quiz_id, methods=["POST"]):
    # fonction pour créer et modifier un quizz
    # on vérifie dans la BD si il y'a des questions dans le qcm
    # pour savoir si on crée ou on edit un quizz
    return render_template(
        "editQuiz.html",
        title="Editer : "+Quiz.query.get(quiz_id).nom,
    )


@app.route("/profile/<int:IDuser>/myquizz/")
def my_quizz(IDuser):
    pass

@app.route("/profile/<int:IDuser>/")
def profile(IDuser):
    pass