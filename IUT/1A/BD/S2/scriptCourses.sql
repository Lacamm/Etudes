DROP TABLE IF EXISTS EFFECTUER;
DROP TABLE IF EXISTS COURSE;
DROP TABLE IF EXISTS COUREUR;
DROP TABLE IF EXISTS CATEGORIE;
DROP TABLE IF EXISTS CLUB;
DROP TABLE IF EXISTS EVENEMENT;
DROP TABLE IF EXISTS LIEU;

/* Creation des tables */
CREATE TABLE LIEU(
	idL INT,
	nomL VARCHAR(30),
	PRIMARY KEY(idL)
);

CREATE TABLE EVENEMENT(
    idEv INT,
    nomEv VARCHAR(30),
    dateEv DATE,
    idL INT,
    PRIMARY KEY(idEv),
	FOREIGN KEY (idL) REFERENCES LIEU(idL)
);
    
CREATE TABLE CLUB(
	idCl INT,
	sigleCL VARCHAR(5),
	nomCl VARCHAR(30),
	PRIMARY KEY(idCl)
);

CREATE TABLE CATEGORIE(
	idCat INT,
	nomCat VARCHAR(30),
	PRIMARY KEY(idCat)
);

CREATE TABLE COUREUR(
	idCo INT,
	nomCo VARCHAR(20),
	prenomCo VARCHAR(20),
    idCat INT,
	idCl INT,
	PRIMARY KEY(idCo),
	FOREIGN KEY (idCat) REFERENCES CATEGORIE(idCat),
	FOREIGN KEY (idCl) REFERENCES CLUB(idCl)
);

CREATE TABLE COURSE(
	idEv INT,
	idCourse INT,
	heure DATETIME,
	idCat INT,
	PRIMARY KEY(idEv, idCourse),
	FOREIGN KEY (idEv) REFERENCES EVENEMENT(idEv),
	FOREIGN KEY (idCat) REFERENCES CATEGORIE(idCat)
);

CREATE TABLE EFFECTUER(
	idCo INT,
	idEv INT,
	idCourse INT,
	temps DATETIME,
	PRIMARY KEY(idCo, idEv, idCourse),
	FOREIGN KEY (idCo) REFERENCES COUREUR(idCo),
	FOREIGN KEY (idEv, idCourse) REFERENCES COURSE(idEv, idCourse)
);

-- Insertion des donnees pour Dupont Jean du club USO a couru  
-- les Foulée d'Orléans en Sénior le 12/12/15 à 9h en 12 minutes 32 secondes 
--  dans les tables 
INSERT INTO CLUB VALUES
	(1, "USO", "Club de l'USO");

INSERT INTO LIEU VALUES
	(1, "Orleans");
    
INSERT INTO EVENEMENT VALUES
    (1, "Foulees d’Orleans", STR_TO_DATE('12/12/2015', '%d/%m/%Y'), 1);

INSERT INTO CATEGORIE VALUES
	(1, "Senior");
    
INSERT INTO COURSE VALUES 
    (1, 1, STR_TO_DATE('09:00', '%h:%i'),1);
    
INSERT INTO COUREUR VALUES
	(1, "Dupont", "Jean", 1, 1);

INSERT INTO EFFECTUER VALUES
	(1, 1, 1, STR_TO_DATE('12:32', '%i:%s'));

-- Insertion des donnees pour Duval Marie, qui est junior a l'ASM, a couru 
-- la corida d'Olivet en Sénior le 25/12/15 à 11h en 11 minutes 53 secondes 
-- et le Cross'O d'Orléans en 8 minutes 59 s 
INSERT INTO CLUB VALUES
	(2, "ASM", "Club de l'ASM");

INSERT INTO LIEU VALUES
	(2, "Olivet");
    
INSERT INTO EVENEMENT VALUES
    (2, "Corida", STR_TO_DATE('25/12/2015', '%d/%m/%Y'), 2),
    (3, "Cross'O", STR_TO_DATE('01/01/2016', '%d/%m/%Y'), 1);

INSERT INTO CATEGORIE VALUES
	(2, "Junior");
    
INSERT INTO COURSE VALUES 
    (2, 1, STR_TO_DATE('11:00', '%h:%i'),2),
    (3, 1, STR_TO_DATE('10:00', '%h:%i'),2);
    
    
INSERT INTO COUREUR VALUES
	(2, "Duval", "Marie", 2, 2);

INSERT INTO EFFECTUER VALUES
	(2, 2, 1, STR_TO_DATE('11:53', '%i:%s')),
 	(2, 3, 1, STR_TO_DATE('08:59', '%i:%s'));
   
-- Insertion des donnees pour Vite-Tours à Tours pour les sénior 
-- le 18/03:16 à 9h pour les séniors et 10h30 pour les juniors 
INSERT INTO LIEU VALUES
	(3, "Tours");
    
INSERT INTO EVENEMENT VALUES
    (4, "Vite-Tours", STR_TO_DATE('18/03/2016', '%d/%m/%Y'), 3);

INSERT INTO COURSE VALUES 
    (4, 1, STR_TO_DATE('09:00', '%h:%i'),1),
    (4, 2, STR_TO_DATE('10:30', '%h:%i'),2);  
    
-- Delete from CLUB where sigleCL = "USO";

      
/* Insertion d'autres donnees dans les tables */

INSERT INTO COUREUR VALUES
	(3, "Dupond", "Pierre", 2, 1),
	(4, "Dupont", "Carine", 2, 2),
	(5, "Richardson", "Mike", 1, 1);

INSERT INTO EFFECTUER VALUES
	(3, 2, 1, STR_TO_DATE('10:53', '%i:%s')),
 	(3, 3, 1, STR_TO_DATE('18:59', '%i:%s')),
 	(4, 3, 1, STR_TO_DATE('12:59', '%i:%s'));
    

-- R1
select *
from EVENEMENT natural join LIEU
where nomL='Orleans'
order by nomEv;

-- R2
INSERT INTO COUREUR VALUES
	(8, "Paolus", "Romain", 1, 1);
INSERT INTO EFFECTUER VALUES
	(8, 1, 1, STR_TO_DATE('10:32', '%i:%s'));

--R2
select idCo, NomCo, time(temps)
from COUREUR natural join EFFECTUER natural join CLUB natural join CATEGORIE natural join EVENEMENT natural join LIEU
where nomEv = "Foulees d’Orleans" and nomCat = 'Senior' and sigleCL='USO'
order by temps desc;


