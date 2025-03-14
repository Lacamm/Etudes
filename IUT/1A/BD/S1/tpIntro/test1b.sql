drop table BDHabitantVoiture;

create table BDHabitantVoiture(
Id number(2),
Prenom Varchar2(20),
Nom Varchar2(20),
Sexe Varchar2(1),
Rue Varchar2(20),
Num Number(2),
Ville Varchar2(10),
MarqueV Varchar2(10),
NomV Varchar2(10),
AnneeV Number(4),
CouleurV Varchar2(10),
TypeMoteurV Varchar2(10),
ImmV Varchar2(10),
constraint CleGrandTableVoiture PRIMARY KEY (ImmV),
constraint CleGrandTablePersonne UNIQUE (id)
);

-- Script pour inserer differentes valeurs dans dans la table BdHabitantVoiture

insert into BdHabitantVoiture values (1, 'Arlette', 'Fort', 'F',
 'des Allouettes', 15, 'Olivet', 'Renault', 'Zoe', 2016, 
 'blanche', 'electrique', 'AD-123-EF');

insert into BdHabitantVoiture values (2, 'Arlette', 'Fort', 'F', 
'Alesia', 4, 'Paris', 'Renault', 'Clio', 2017, 
'blanche', 'essence', 'AB-333-CC');
