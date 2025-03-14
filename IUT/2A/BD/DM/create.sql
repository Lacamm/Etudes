drop table PATHOLOGIE cascade constraints;
drop table CONSULTATION cascade constraints;
drop table PLANNING_OPE cascade constraints;
drop table MEDECIN_OPE cascade constraints;
drop table RESPONSABLE_OPE cascade constraints;
drop table IDENTIFIANT_OPE cascade constraints;
drop table OPERATION cascade constraints;
drop table MEDECIN cascade constraints;
drop table PATIENT cascade constraints;
drop table PERSONNE cascade constraints;


create table PERSONNE
(id number(10),
nom VarChar2(20),
prenom VarChar2(20),
ad VarChar2(30),
tel number(10),
constraint KPERSONNE primary key (id));

create table PATIENT
(idPat number(10),
numSec number(13),
dateNais Date,
constraint KPATIENT primary key (idPat));

create table MEDECIN
(idMed   number(10),
grade  VarChar2(30),
bureau  VarChar2(10),
poste   VarChar2(20),
domSpec   VarChar2(50),
constraint KMEDECIN primary key (idMed));
Constraint UBUREAU UNIQUE (bureau);
constraint KMEDECIN primary key (idMed));

create table PATHOLOGIE
(pato VarChar2(50),
domSpec VarChar2(50),
constraint KPATHOLOGIE primary key (pato));


create table OPERATION
( idPat number(10),
dateOp Date,
refOp   VarChar2(5),
salleOp  VarChar2(2),
heureDebOp Date,
heureFinOp  Date,
DescripOp  VarChar2(150),
pato  VarChar2(50),
idResp  number(10),
nomContact  VarChar2(20),
telContact number(10),
situation VarChar2(50),
derniereMaj  Date,
constraint KOPERATION primary key (idPat,dateOp));

create table IDENTIFIANT_OPE
( dateOp Date,
refOp   VarChar2(5),
salleOp  VarChar2(2),
idPat number(10),
constraint KIDENTIFIANT_OPE primary key (dateOp,refOp,salleOp));

create table RESPONSABLE_OPE
( idResp number(10),
dateOp  Date,
heureDebOp  Date,
idPat number(10),
constraint KRESPONSABLE_OPE primary key (idResp, dateOp, heureDebOp));

create table MEDECIN_OPE
( idMed number(10),
dateOp   Date,
heureDebOp  Date,
idPat number(10),
constraint KMEDECIN_OPE primary key (idMed, dateOp, heureDebOp));

create table PLANNING_OPE 
( dateOp Date,
heureDebOp Date,
salleOp  VarChar2(2),
idPat  number(10),
constraint KPLANNING_OPE primary key (dateOp, heureDebOp, salleOp));

create table CONSULTATION
( idMed number(10),
dateCons  Date,
plageHCons Date,
numCons  number(1),
idPat  number(10),
dateOp  Date,
constraint KCONSULTATION primary key (idMed, dateCons, plageHCons, numCons));


ALTER TABLE OPERATION ADD FOREIGN KEY (idPat) REFERENCES PATIENT (idPat);
ALTER TABLE IDENTIFIANT_OPE ADD FOREIGN KEY (idPat) REFERENCES PATIENT (idPat);
ALTER TABLE RESPONSABLE_OPE ADD FOREIGN KEY (idPat) REFERENCES PATIENT (idPat);
ALTER TABLE MEDECIN_OPE ADD FOREIGN KEY (idPat) REFERENCES PATIENT (idPat);
ALTER TABLE PLANNING_OPE ADD FOREIGN KEY (idPat) REFERENCES PATIENT (idPat);
ALTER TABLE CONSULTATION ADD FOREIGN KEY (idPat) REFERENCES PATIENT (idPat);

ALTER TABLE CONSULTATION ADD FOREIGN KEY (idMed) REFERENCES MEDECIN (idMed);
ALTER TABLE MEDECIN_OPE ADD FOREIGN KEY (idMed) REFERENCES MEDECIN (idMed);

ALTER TABLE OPERATION ADD FOREIGN KEY (pato) REFERENCES PATHOLOGIE (pato);

ALTER TABLE IDENTIFIANT_OPE ADD FOREIGN KEY (idPat,dateOp) REFERENCES OPERATION (idPat,dateOp);
ALTER TABLE RESPONSABLE_OPE ADD FOREIGN KEY (idPat,dateOp) REFERENCES OPERATION (idPat,dateOp);
ALTER TABLE MEDECIN_OPE ADD FOREIGN KEY (idPat,dateOp) REFERENCES OPERATION (idPat,dateOp);
ALTER TABLE PLANNING_OPE ADD FOREIGN KEY (idPat,dateOp) REFERENCES OPERATION (idPat,dateOp);
ALTER TABLE CONSULTATION ADD FOREIGN KEY (idPat,dateOp) REFERENCES OPERATION (idPat,dateOp);

ALTER TABLE OPERATION ADD FOREIGN KEY (dateOp,refOp,salleOp) REFERENCES IDENTIFIANT_OPE (dateOp,refOp,salleOp);

ALTER TABLE OPERATION ADD FOREIGN KEY (idResp, dateOp, heureDebOp) REFERENCES RESPONSABLE_OPE (idResp, dateOp, heureDebOp);

ALTER TABLE OPERATION ADD FOREIGN KEY (dateOp, heureDebOp, salleOp) REFERENCES PLANNING_OPE (dateOp, heureDebOp, salleOp);
