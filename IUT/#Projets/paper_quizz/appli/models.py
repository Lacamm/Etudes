from .app import db, login_manager
from flask_login import UserMixin
from hashlib import sha256

####################### db #######################


class Utilisateur(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    identifiant = db.Column(db.String(64), unique=True)
    prenom = db.Column(db.String(64))
    nom = db.Column(db.String(64))
    email = db.Column(db.String(64))
    mdp = db.Column(db.String(64))
    estProf = db.Column(db.Boolean())

    def get_id(self):
        return self.identifiant

    def __repr__(self):
        return "<Utilisateur (%d) %s>" % (self.id, self.identifiant)

class Etre_Resp(db.Model):
    idUser = db.Column(db.Integer, db.ForeignKey("utilisateur.id"), primary_key=True)
    utilisateur = db.relationship("Utilisateur", backref=db.backref("responsables", lazy="dynamic"))
    idQuiz = db.Column(db.Integer, db.ForeignKey("quiz.id"), primary_key=True)
    quiz = db.relationship("Quiz", backref=db.backref("responsables", lazy="dynamic"))

    def __repr__(self):
        return "<L'utilisateur %d est responsable du quizz %d)>" % (self.idUser, self.idQuiz)

class TypeQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intitule = db.Column(db.Text)
    
    def __repr__(self):
        return "<TypeQ (%d) %s>" %(self.id, self.intitule)

class Categorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categorie = db.Column(db.String(64))

    def __repr__(self):
        return "<Categorie (%d) %s>" % (self.id,self.categorie)

class Reponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intitule = db.Column(db.Text())
    coef = db.Column(db.Float())
    idQuestion = db.Column(db.Integer, db.ForeignKey("question.id"))
    question = db.relationship("Question", backref=db.backref("reponses", lazy="dynamic"))
    
    def __repr__(self):
        return "<Reponse (%d) %s>" %(self.id, self.intitule)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    intitule = db.Column(db.Text())
    points = db.Column(db.Integer)
    idCat = db.Column(db.Integer, db.ForeignKey("categorie.id"))
    categorie = db.relationship("Categorie", backref=db.backref("questions", lazy="dynamic"))
    idTypeQ = db.Column(db.Integer, db.ForeignKey("typeQ.id"))
    typeQ = db.relationship("TypeQ", backref=db.backref("questions", lazy="dynamic"))

    def __repr__(self):
        return "<Question (%d) %s>" % (self.id, self.intitule)

class Composer(db.Model):
    idQuestion = db.Column(db.Integer, db.ForeignKey("question.id"), primary_key=True)
    question = db.relationship("Question", backref=db.backref("compose", lazy="dynamic"))
    idQuiz = db.Column(db.Integer, db.ForeignKey("quiz.id"), primary_key=True)
    quiz = db.relationship("Quiz", backref=db.backref("composeDe", lazy="dynamic"))

    def __repr__(self):
        return "<La question %d compose le quiz %d>" % (self.idQuestion,self.idQuiz)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(64))
    mdp = db.Column(db.String(64))
    creation = db.Column(db.Date)
    debut = db.Column(db.Date)
    fin = db.Column(db.Date)
    duree = db.Column(db.Integer)
    
    def __repr__(self):
        return "<Quiz (%d) %s>" %(self.id, self.nom)

class Participation(db.Model):
    idUser = db.Column(db.Integer, db.ForeignKey("utilisateur.id"), 
            primary_key=True)
    utilisateur = db.relationship("Utilisateur", foreign_keys=[idUser], 
            backref=db.backref("user", lazy="dynamic"))

    idQuiz = db.Column(db.Integer, db.ForeignKey("quiz.id"), 
            primary_key=True)
    quiz = db.relationship("Quiz", foreign_keys=[idQuiz], 
            backref=db.backref("quiz", lazy="dynamic"))

#     numeroParticipation = db.Column(db.Integer, 
#             primary_key=True)
    
#     dateParticipation = db.Column(db.Date)

# class Repondre(db.Model):
#     idUser = db.Column(db.Integer, db.ForeignKey("participation.idUser"), primary_key=True)
#     idQuiz = db.Column(db.Integer, db.ForeignKey("participation.idQuiz"), primary_key=True)
#     numeroParticipation = db.Column(db.Integer, db.ForeignKey("participation.numeroParticipation"), primary_key=True)
#     participation = db.relationship("Participation", foreign_keys=[idUser,idQuiz,numeroParticipation], backref=db.backref("participation", lazy="dynamic"))

#     idReponse = db.Column(db.Integer, primary_key=True)
#     reponse = db.relationship("Reponse", backref=db.backref("reponse", lazy="dynamic"))

#     def __repr__(self):
#         return "<Repondre (%d) %s>" %(self.id, self.nom)


##################################################


################## Utilisateur ###################


def get_utilisateurByIdentifiant(identifiant):
    return Utilisateur.query.filter(Utilisateur.identifiant==identifiant).first()

@login_manager.user_loader
def load_user(username):
    return Utilisateur.query.filter(Utilisateur.identifiant==username).first()

def add_user(identifiant, prenom, nom, email, mdp, role="etu"):
    """
    Adds a new user.
    """
    m = sha256()
    m.update(mdp.encode())
    estProf = (role == "Prof" or role == "prof")
    user = Utilisateur(
        identifiant = identifiant,
        prenom = prenom,
        nom = nom,
        email = email,
        mdp = m.hexdigest(),
        estProf = estProf
    )
    db.session.add(user)
    db.session.commit()
    return user


##################################################


##################################################


def get_allQuiz():
    return Quiz.query.all()

def get_questionsByQuizId(quiz_id):
    return Question.query.filter(Question.compose.idQuiz==quiz_id).all


##################################################


def questionsDunquizz(idQuiz):
    return Composer.query.filter(Composer.idQuiz==idQuiz).compose.all()
    # res = []
    # for instance in Composer.query.filter(Composer.idQuiz.like(idQuiz))
    #     res.append(instance.question)

def getQuestions():
    return Question.query.order_by(Question.id).all()

def get_questionRecherche(recherche):
    return Question.query.filter(Question.intitule.like('%'+recherche+'%')).all()

def getTypeQuestionById():
    id = Question.query.idTypeQ
    return TypeQ.query.get(id).intitule

def getReponseByIdQuestion(idQuestion):
    return Reponse.query.get(idQuestion)
