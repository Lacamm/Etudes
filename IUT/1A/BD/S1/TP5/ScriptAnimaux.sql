drop table Classement;
drop table Concours;
drop table Animaux;
drop table Proprietaires;

create table Proprietaires
(Id Number(4)  primary key, 
Nom VarChar2(20),  
Prenom  VarChar2(20),
Ville Varchar2(20));

create table Animaux
(Prop Number(4),
NomAnimal VarChar2(20),  
Type VarChar2(10),  
Race VarChar2(10),  
Categorie VarChar2(10), 
DateNais date,
constraint keyAnimal primary key (Prop,NomAnimal),
constraint FKproprietaire foreign key (Prop) references Proprietaires (Id)); 

create table Concours
(Titre Varchar2(20),
Annee  date,
Categorie Varchar2(10),
Certificat Varchar2(20),
TypeConcours Varchar2(3),
Ville Varchar2(20),
check (TypeConcours = 'INT' or TypeConcours = 'NAT'),
constraint keyConcours primary key (Titre, Annee),
constraint uniqueConcours unique (Ville, Annee, Categorie));


create table Classement
(Prop Number(4) , 
Animal VarChar2(20), 
TitreC Varchar2(20),
AnneeC  date, 
PositionClassement number(3),
constraint KEYClassement primary key (Prop, Animal, TitreC, AnneeC),
constraint FKPropClassement foreign key (Prop) references Proprietaires(Id) on delete cascade,
constraint FKAnimalClassement foreign key (Prop, Animal) references Animaux(Prop,NomAnimal) on delete cascade,
constraint FKConcoursClassement foreign key (TitreC,AnneeC) references Concours(Titre, Annee) on delete cascade);


insert into Proprietaires values (1,'Niarchos','Maxime','Orléans');
insert into Animaux values (1,'Bargos','Cheval','Charal','Course',to_date('2001','YYYY'));
