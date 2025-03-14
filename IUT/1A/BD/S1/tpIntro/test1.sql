drop table BDHabitantVoiture;

create table BDHabitantVoiture(
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
ImmV Varchar2(10)
);

insert into BdHabitantVoiture values ('Arlette','Fort','F',
'des Allouettes',15,'Olivet', 'Renault','Zoe',2016,'blanche',
'electrique','AD-123-EF');

insert into BDHabitantVoiture values ('Jean','Duprack','M',
'des Allouettes',12,'Olivet','Peugeot','2008',2015,'noire',
'essence','AD-234-EF');

insert into BDHabitantVoiture values ('Arlette','Fort','F',
'Alesia',4,'Paris','Renault','Clio',2017,'blanche','essence',
'AB-333-CC');

insert into BDHabitantVoiture values ('Arlette','Fort','F',
'des Allouettes',15,'Olivet','Renault','Clio',2017,'rouge',
'essence','AD-567-EF');

insert into BDHabitantVoiture values ('Jean','Dubois','M',
'Rivoli',12,'Paris','Peugeot','2008',2015,'noire','essence',
'AD-333-EF');

insert into BDHabitantVoiture values ('Jean','Dubois','M',
'Rivoli',12,'Paris','Renault','Clio',2017,'noire','essence',
'AD-444-EF');

insert into BDHabitantVoiture values ('Jean','Dubois','M',
'Rivoli',12,'Paris','Toyota','Verso',2015,'bleu','diesel',
'AA-333-BB');

insert into BDHabitantVoiture values ('Jean','Dubois','M',
'Rivoli',12,'Paris','Toyota','Yaris',2017,'rouge','hybrid',
'AA-333-BB');
