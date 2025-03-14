/*Exercice 1*/

	/*Question1*/

create or replace view Produit10 as
select refProd, nomProd, PUProd
from PRODUIT
where PUProd > 10;

select * from Produit10;

	/*Question 2*/

create or replace view DixMars2015 as
select refProd, nomProd, PUProd
from PRODUIT natural join DETAIL natural join FACTURE
where dateFac = STR_TO_DATE('10-03-2015','%d-%m-%Y');

select * from DixMars2015;

	/*Question 3*/
	
create or replace view NbClientsParVille(ville, nbCli) as
select adresseCli, count(numCli)
from CLIENT
group by adresseCli;

select * from NbClientsParVille
where ville like 'M%';

	/*Question 4*/

create or replace view CAParMois as
select month(dateFac)mois, year(dateFac) annee,sum(PUProd*qte) CA 
from PRODUIT natural join DETAIL natural join FACTURE 
where year(dateFac) like '%2015'
group by mois, annee
order by annee, mois;

select * from CAParMois;

	/*Question 5*/

DROP VIEW Produit10;
DROP VIEW DixMars2015;
DROP VIEW NbClientsParVille;
DROP VIEW CAParMois;

/*Exercice 2*/

	/*Question 1*/

prepare supPrix from
'select *
from PRODUIT
where PUProd >= ?';

set @prix:=10;
execute supPrix using @prix;

	/*Question 2*/

prepare laFacture from
'select refProd, nomProd, PUProd, qte
from FACTURE natural join DETAIL natural join PRODUIT
where numFac=?';

set @nfacture:= 221;
execute laFacture using @nfacture;

/*Exercice 3*/

	/*Question 1*/
	
select nomProd
from PRODUIT natural left join DETAIL
where numFac is null;

	/*Question 2*/

select nomProd, count(numFac) as nbFac
from PRODUIT natural left join DETAIL
where nomProd like 'M%'
group by nomProd;

	/*Question 3*/

select nomProd, IFNULL(sum(qte), 0) as qteTotale
from PRODUIT natural left join DETAIL
where nomProd like 'M%'
group by nomProd;

/*Exercice 4*/

	/*Question 1*/

create or replace view Annee as
select distinct Year(dateFac) as annee
from FACTURE
group by dateFac;



create or replace view ClientAnnee as
select annee, numCli, nomCli, prenomCli
from CLIENT, Annee;

create or replace view CAParClientParAn as
select numCLi, Year(dateFac) annee, sum(Qte*PUProd) as CA
from FACTURE natural join DETAIL natural join PRODUIT
group by numCli, YEAR(dateFac);

create or replace view CAParClientParAn0 as
select distinct annee, numCli, nomCli, prenomCli, IFNULL(CA, 0) as CA
from ClientAnnee natural left join CAParClientParAn;

select * from Annee;
select * from ClientAnnee;
select * from CAParClientParAn0 where nomCli='ZET' and prenomCli='Mathieu';
	
	/*Question 2*/


create or replace view ProdAnnee as
select annee, refProd, nomProd
from PRODUIT, Annee;

create or replace view CAParProdAn as
select refProd, Year(dateFac) annee, sum(Qte*PUProd) as CA
from FACTURE natural join DETAIL natural join PRODUIT
group by refProd, YEAR(dateFac);

create or replace view CAParProdAn0 as
select distinct annee, refProd, nomProd, IFNULL(CA, 0) as CA
from ProdAnnee natural left join CAParProdAn;

select * from ProdAnnee;
select * from CAParProdAn;
select * from CAParProdAn0 where nomProd like 'T%';











