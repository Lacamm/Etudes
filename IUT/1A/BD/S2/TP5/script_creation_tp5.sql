drop table if exists EFFECTUER;
drop table if exists COUREUR;
drop table if exists CLUB;
drop table if exists COURSE;
drop table if exists CATEGORIE;
drop table if exists EVENEMENT;
drop table if exists LIEU;

CREATE TABLE LIEU (
idL  	int,
nomL 	varchar(30),
PRIMARY KEY (idL)
);

CREATE TABLE COURSE(
idCourse int,
heure time,
PRIMARY KEY(idCourse),
idEv int,
idCat int
);

CREATE TABLE EFFECTUER(
  temps time,
  idCo int,
  idEv int,
  idCourse int
);

CREATE TABLE COUREUR(
  idCo int,
  nomCo varchar(20),
  prenomCo varchar(20),
  PRIMARY KEY(idCo),
  idCat int,
  idCl int
);

CREATE TABLE CLUB(
  idCl int,
  sigleCL varchar(10),
  nomCL varchar(50),
  PRIMARY KEY(idCl)
);

CREATE TABLE CATEGORIE(
  idCat int,
  nomCat varchar(20),
  PRIMARY KEY(idCat)
);

CREATE TABLE EVENEMENT(
idEv    int,
nomEv 	varchar(50),
dateEv 	date,
idL		int,
PRIMARY KEY (idEv),
FOREIGN KEY (idL) REFERENCES LIEU (idL)
);


ALTER TABLE EVENEMENT ADD FOREIGN KEY (idL) REFERENCES LIEU(idL) on delete cascade;

ALTER TABLE COURSE ADD FOREIGN KEY (idEv) REFERENCES EVENEMENT(idEv) on delete cascade;
ALTER TABLE COURSE ADD FOREIGN KEY (idCat) REFERENCES CATEGORIE(idCat) on delete cascade;

ALTER TABLE EFFECTUER ADD FOREIGN KEY (idCo) REFERENCES COUREUR(idCo) on delete cascade;
ALTER TABLE EFFECTUER ADD FOREIGN KEY (idEv, idCourse) REFERENCES COURSE(idEv, idCourse)on delete cascade;

ALTER TABLE COUREUR ADD FOREIGN KEY (idCat) REFERENCES CATEGORIE(idCat) on delete cascade;
ALTER TABLE COUREUR ADD FOREIGN KEY (idCl) REFERENCES CLUB(idCl) on delete cascade;
