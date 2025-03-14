DROP TABLE VENTE;
DROP TABLE CATEGORIE;
DROP TABLE PHOTO;
DROP TABLE PROPOSITION;
DROP TABLE OBJET;
DROP TABLE TYPEDROIT;
DROP TABLE MESSAGES;
DROP TABLE COMPORTE;
DROP TABLE UTILISATEUR;
DROP TABLE PROFIL;

CREATE TABLE MESSAGES(
    idM int,
    contenuMessage varchar(150),
    messagelu boolean,
    dateM date,
    heureM time,
    PRIMARY KEY (idM)
);
CREATE TABLE UTILISATEUR(
    idU int,
    pseudo varchar(20),
    mdp varchar(16),
    actif boolean,
    PRIMARY KEY (idU)
);
CREATE TABLE PROFIL(
    pseudo varchar(20),
    nomU varchar(20),
    prenomU varchar(20),
    mail varchar(40),
    PRIMARY KEY (pseudo)
);
CREATE TABLE TYPEDROIT(
    idT int,
    intituleDroit varchar(20),
    PRIMARY KEY (idT)
);
CREATE TABLE OBJET(
    idO int,
    nomO varchar(20),
    descrip varchar(200),
    prixDep int,
    prixFin int,
    PRIMARY KEY (idO)
);
CREATE TABLE PROPOSITION(
    idP int,
    dateProp date,
    heureP time,
    montantProp int,
    PRIMARY KEY (idP)
);
CREATE TABLE PHOTO(
    idPhoto int,
    nomPhoto varchar(20),
    urlphoto varchar(100),
    PRIMARY KEY (idPhoto)
);
CREATE TABLE CATEGORIE(
    idCat int, 
    nomCat varchar(30),
    PRIMARY KEY (idCat)
);
CREATE TABLE VENTE(
    idVente int,
    heureDeb time,
    heureFin time,
    dateDeb date,
    dateFin date,
    etatVente varchar(30),
    idAcquereur int,
    PRIMARY KEY (idVente)
);
CREATE TABLE COMPORTE(
    pseudo varchar(30),
    idU int,
    PRIMARY KEY(pseudo,idU)
);

ALTER TABLE UTILISATEUR ADD FOREIGN KEY (pseudo) REFERENCES PROFIL (pseudo);
ALTER TABLE COMPORTE ADD FOREIGN KEY (pseudo) REFERENCES PROFIL (pseudo);
ALTER TABLE COMPORTE ADD FOREIGN KEY (idU) REFERENCES UTILISATEUR (idU);



insert into MESSAGES (idM,contenuMessage,messagelu,dateM,heureM) values
    (01,'Bienvenue sur nos encheres',1,STR_TO_DATE('21/09/19','%d/%m/%Y'),STR_TO_DATE('15:30','%H:%i')),
    (02,'La semaine des encheres approche...',0,STR_TO_DATE('15/10/19','%d/%m/%Y'),STR_TO_DATE('08:15','%H:%i'));
insert into PROFIL (pseudo,nomU,prenomU,mail) values
    ('iuto','Jean','Dupond','j.dupond@admin.fr'),
    ('iuto2','Rachelle','Martin','r.martin@user.fr');
insert into UTILISATEUR (idU,pseudo,mdp,actif) values
    (01,'iuto','mdp',0),
    (02,'iuto2','azerty',0);
insert into TYPEDROIT (idT,intituleDroit) values
    (01,'admin'),
    (02,'utilisateur');
insert into OBJET (idO,nomO,descrip,prixDep,prixFin) values
    (0001,'Lampe','une lampe de chevet..',5,15),
    (0002,'Table','Une table pour votre salle a manger',15,30),
    (003,'Ordinateur','Un ordinateur pour votre Bureau',50,150);
insert into PROPOSITION (idP,dateProp,heureP,montantProp)values
    (0001,STR_TO_DATE('20/10/19','%d/%m/%Y'),STR_TO_DATE('12:25','%H:%i'),20),
    (0002,STR_TO_DATE('20/10/19','%d/%m/%Y'),STR_TO_DATE('12:30','%H:%i'),30);
insert into PHOTO (idPhoto,nomPhoto,urlphoto) values
    (0001,'lampe.png','https://www.google.fr/search?q=img&client=ubuntu-browser&source=lnms&tbm'),
    (0002,'table.png','https://www.google.fr/search?q=img&client=ubuntu-browser&source=lnms&tbfdhgfyedb');
insert into CATEGORIE (idCat,nomCat) values 
    (0001,'meubles'),
    (0002,'Materiel Informatique');
insert into VENTE (idVente,dateDeb,heureDeb,dateFin,heureFin,etatVente,idAcquereur) values
    (0001,STR_TO_DATE('21/10/19','%d/%m/%Y'),STR_TO_DATE('8:00','%H:%i'),STR_TO_DATE('21/10/19','%d/%m/%Y'),STR_TO_DATE('18:00','%H:%i'),'Terminée',001);

insert into COMPORTE(pseudo,idU) values
    ("iuto",01),
    ('iuto2',02);
