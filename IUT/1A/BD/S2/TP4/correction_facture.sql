-- EXERCICE 1

-- Creation des Vues

create or replace view Produit10 as 
select refProd, nomProd, PUProd
from PRODUIT
where PUProd >10;

create or replace view DixMars2015 as 
select refProd, nomProd, PUProd
from PRODUIT natural join DETAIL natural join FACTURE
where  dateFac= STR_TO_DATE('10-03-2015','%d-%m-%Y');

create or replace view NbClientsParVille(ville, NbCli) as
select adresseCli, count(numCli)
from CLIENT
group by adresseCli;

create or replace view CAParMois as
select month(dateFac)mois, year(dateFac) annee,sum(PUProd*qte) CA 
from PRODUIT natural join DETAIL natural join FACTURE 
where year(dateFac) like '%2015' group by mois;

-- Affichage des Vues

select * from Produit10;
select * from DixMars2015;
select *from NbClientsParVille where ville like 'M%';
select * from CAParMois;

-- Suppression des Vues

DROP VIEW Produit10;
DROP VIEW DixMars2015;
DROP VIEW NbClientsParVille;
DROP VIEW CAParMois;

-- EXERCICE 2

prepare Prix from 
'select refProd, nomProd, PUprod
from PRODUIT 
where PUProd>?';
set @prix := 10;
execute Prix using @prix;

prepare Facture from
'select refProd, nomProd, PUprod, qte
from FACTURE natural join DETAIL natural join PRODUIT
Where numFac=?';
set @facture := 221;
execute Facture using @facture;

-- EXERICE 3

select nomProd
from PRODUIT natural left join DETAIL
where numFac is null;

select nomProd, count(numFac) nbFac
from PRODUIT natural left join DETAIL
where nomProd like 'M%'
group by nomProd;

select nomProd, IFNULL(sum(qte), 0) qteTotal
from PRODUIT natural left join DETAIL
where nomProd like 'M%'
group by nomProd;

-- EXERICE 4

create or replace view Annee as
select distinct Year(dateFac) annee
from FACTURE
group by dateFac;

create or replace view ClientAnnee as
select annee, numCli
from Annee natural join CLIENT;

select * from Annee;
select * from ClientAnnee;
