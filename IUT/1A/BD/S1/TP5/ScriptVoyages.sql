drop table Activite;
drop table Client;
drop table Sejour;
drop table Station;

create table Station
(nomStation VarChar2(20) primary key,
capacite Number(3) not null,
lieu VarChar2(20) not null,
region Varchar2(20),
tarif Number(4) default 0,
constraint UniqueStation unique (lieu, region),
check (region = 'Océan Indien Antilles' or region = 'Europe' or region = 'Ameriques' or region = 'Extreme Orient'));

create table Activite
(libelle VarChar2(20) primary key,
nomStation VarChar2(20),
prix Number(3) default 0,
constraint FKnomStation foreign key (nomStation) references Station(nomStation) on delete cascade);

create table Client
(id Number(2) primary key,
nom VarChar2(15) not null,
prenom VarChar2(20),
ville VarChar2(20) not null,
region VarChar2(20),
solde Number(4) default 0,
check (region = 'Océan Indien Antilles' or region = 'Europe' or region = 'Ameriques' or region = 'Extreme Orient'));

create table Sejour
(id Number(2),
debut date,
station VarChar2(20),
nbPlaces Number(1) not null,
constraint keySejour primary key (id, debut),
constraint FKstation foreign key (nomStation) references Station(nomStation) on delete cascade);

