-- @ SCRIPTS/CreateDrop-Journaux;


-- Table pour examen/ seulement contraintes cles primaires


drop table JOURNAUX cascade constraints;
drop table KIOSQUES cascade constraints;
drop table VEND cascade constraints;
drop table AIME cascade constraints;
drop table ACHAT_HABITUEL cascade constraints;
drop table CLIENTS cascade constraints;


create table JOURNAUX
(Titre VarChar2(30),
Type VarChar2(10),
Categorie VarChar2(20),
PrixUnit number(10,2),
constraint KJournaux primary key (Titre));

create table CLIENTS
(IdCl number(3),
Nom VarChar2(20),
Age number(3),
Sexe VarChar2(1),
constraint KeyClient primary key (IdCl));

create table KIOSQUES
(NomK   VarChar2(30),
VilleK  VarChar2(20),
Ad      VarChar2(10),
constraint KClient primary key (NomK, VilleK));


create table VEND
(NomK   VarChar2(30),
VilleK  VarChar2(20),
Titre VarChar2(30));


create table AIME
(IdCl number(3),
Titre VarChar2(30));


create table ACHAT_HABITUEL
( IdCl number(3),
Titre VarChar2(30),
NomK   VarChar2(30),
VilleK  VarChar2(20));


