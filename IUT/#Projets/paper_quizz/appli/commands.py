import click
from .app import app, db
import datetime

import xml.dom.minidom
import xml.etree.ElementTree as ET

@app.cli.command()
def syncdb():
    '''
     Création de toutes les tables de la BD
    '''
    db.create_all()


@app.cli.command()
def dropdb():
    """
    Drop all the tables
    """
    db.drop_all()


@app.cli.command()
def loaddb():
    '''Creates the tables and populates them with data.'''

    # création de toutes les tables
    db.create_all()

    # import des modèles
    from .models import Question, Quiz, TypeQ, Categorie, Composer
    from .models import add_user

    # 0 --- Création d'utilisateurs

    add_user("mickael.hun", "Mickael", "Hun", "mickael.hun@etu.univ-orleans.fr", "123Soleil", role="etu")
    add_user("admin", "admin", "admin", "admin@admin.admin", "admin", role="prof")
    add_user("abc", "abc", "abc", "abc@abc.abc", "abc", role="etu")
    add_user("aze", "aze", "aze", "aze@aze.aze", "aze", role="etu")

    # 1 --- Création des types de question
    
    types = ["simple","multiple","ouvert"]
    for t in types:
        o = TypeQ(intitule=t)
        db.session.add(o)
    db.session.commit()

    # 2 --- Création des categories de question
    categories = ["autre","maths","fr"]
    for c in categories:
        o = Categorie(categorie=c)
        db.session.add(o)
    db.session.commit()

    # 3 --- Création de questions
    for i in range(510):
        question = Question(intitule="Question n°"+str(i+1),
                    points=2,
                    idCat=1,
                    idTypeQ=1
                    )
        db.session.add(question)
    db.session.commit()

    # 4 --- Création de quizz
    for i in range(50):
        quiz = Quiz(
            nom="Quiz"+str(i+1),
            mdp="",
            creation=datetime.datetime.now(),
            debut=datetime.datetime.now(),
            fin=datetime.datetime.now()+datetime.timedelta(days=7),
            duree=3600
        )
        db.session.add(quiz)
    quiz = Quiz(
        nom="Quiz avec mdp",
        mdp="mdp",
        creation=datetime.datetime.now(),
        debut=datetime.datetime.now(),
        fin=datetime.datetime.now()+datetime.timedelta(days=7),
        duree=3600
    )
    db.session.add(quiz)
    db.session.commit()

    # 5 --- Création des relations quiz questions
    quiz_id = 0
    for i in range (0,510):
        if i%10 == 0:
            quiz_id += 1
        o = Composer(idQuestion=i+1, idQuiz=quiz_id)
        db.session.add(o)
    db.session.commit()

    #6 --- Utilisation du xml

    doc = xml.dom.minidom.parse("/home/adrien/projet/code/appli/test.xml")
    tree = ET.parse('/home/adrien/projet/code/appli/test.xml')
    root = tree.getroot()

    if root.tag == "quiz":
        quiz = Quiz(nom="Quiz numéro 1",
        mdp="",
        creation=datetime.date(2020,1,9),
        debut=datetime.date(2020,1,9),
        fin=datetime.date(2020,1,10),
        duree=3600
        )
        db.session.add(quiz)
        db.session.commit()
        for elem in root:
            dg,qt = False,False
            for sub in elem:
                if sub.tag=="questiontext":
                    for subsub in sub:
                        text=subsub.text[3:-4]
                        if text[0] != "<":
                            qt = True
                if sub.tag=="defaultgrade":
                    dg = True
                    pts = sub.text
                if dg and qt:
                    dg,qt = False,False
                    q = Question (intitule=text,
                    points=pts,
                    idCat=0,
                    idTypeQ=elem.get('type'))
                    db.session.add(q)
                    db.session.commit()
    db.session.commit()



@app.cli.command()
@click.argument("identifiant")
@click.argument("nom")
@click.argument("prenom")
@click.argument("email")
@click.argument("mdp")
@click.argument("role")
def newuser(identifiant, prenom, nom, email, mdp, role):
    """
    Adds a new user.
    """
    from .models import Utilisateur
    from hashlib import sha256
    m = sha256()
    m.update(mdp.encode())
    estProf = (role == "Prof" or role == "prof")
    u = Utilisateur(
        identifiant = identifiant,
        prenom = prenom,
        nom = nom,
        email = email,
        mdp = m.hexdigest(),
        estProf = estProf
    )
    db.session.add(u)
    db.session.commit()
