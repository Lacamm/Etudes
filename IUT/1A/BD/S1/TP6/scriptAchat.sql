drop table Client;
drop table Produit;
drop table Commande;
drop table DetailCommande;


create table Client(
IdCli Number(4), 
NomCli Varchar2(20), 
PrenomCli  VarChar2(20), 
Adresse Varchar2(20));
 
create table Produit(
Ref Number(4), 
NomProd Varchar2(20), 
Prix   Number(10,2));

create table  Commande(
NumCom Number(4), 
DateCom Date, 
IdCli   Number(4));

create table DetailCommande(
NumCom Number(4), 
Ref Number(4),   
Quantite Number(4));

insert into Client values ( 1, 'Dupont', 'Jean', 'Orleans');
insert into Client values ( 2, 'Durand', 'Paul', 'Orleans');
insert into Client values ( 3, 'Martin', 'Pierre', 'Olivet');
insert into Client values ( 4, 'Auger', 'Marcel', 'Saint Jean de Braye');


insert into Produit values (1, 'Brosse a dent', 1.2);
insert into Produit values (2, 'Verre', 2.3);
insert into Produit values (3, 'Dentifrice', 1.9);
insert into Produit values (4, 'Savon', 1.4);



insert into Commande values (1, to_date('01-08-2013-21:30','DD-MM-YYYY-HH24:MI'), 1);
insert into Commande values (2, to_date('01-08-2013-8:15','DD-MM-YYYY-HH24:MI'), 2);
insert into Commande values (3, to_date('08-08-2013-12:00','DD-MM-YYYY-HH24:MI'), 1);
insert into Commande values (4, to_date('10-08-201321:30','DD-MM-YYYY-HH24:MI'), 3);
insert into Commande values (5, to_date('10-08-2013-9:10','DD-MM-YYYY-HH24:MI'), 2);
insert into Commande values (6, to_date('11-08-2013-8:15','DD-MM-YYYY-HH24:MI'), 4);
insert into Commande values (7, to_date('11-08-201321:30','DD-MM-YYYY-HH24:MI'), 4);






insert into DetailCommande values (1,1,2);
insert into DetailCommande values (1,2,3);
insert into DetailCommande values (2,1,1);
insert into DetailCommande values (2,4,1);
insert into DetailCommande values (2,3,1);
insert into DetailCommande values (3,3,2);
insert into DetailCommande values (4,1,1);
insert into DetailCommande values (4,2,4);
insert into DetailCommande values (5,3,3);
insert into DetailCommande values (5,4,1);
insert into DetailCommande values (6,1,2);
insert into DetailCommande values (7,4,5);
insert into DetailCommande values (7,3,2);
insert into DetailCommande values (7,1,1);

commit;
