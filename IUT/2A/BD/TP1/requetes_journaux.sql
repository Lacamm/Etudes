-- @ SCRIPTS/requetesJOURNAUX;

--1--
select distinct K1.VilleK, K2.VilleK, K1.NomK 
from KIOSQUES K1, KIOSQUES K2 
where K1.VilleK != K2.VilleK and K1.Nomk=K2.NomK;

--2--
select NomK, VilleK, count(Titre) as total
from VEND 
where VilleK='Orleans' 
group by NomK, VilleK
having count(Titre) > 4;

--3--
select Categorie, avg(PrixUnit) as PrixMoyen
from JOURNAUX
group by Categorie;

--4--
select Categorie, avg(PrixUnit) prixMoyen
from JOURNAUX
group by Categorie
having avg(PrixUnit)>=ALL(select avg(PrixUnit)
                        from JOURNAUX
                        group by Categorie);
                        
--5--
select NomK, VilleK, Categorie, count(Titre) nbJournaux
from VEND natural join JOURNAUX
group by Categorie, NomK, VilleK
order by VilleK, NomK;



--6--
select C.IdCl, C.Nom
from Cient C
where not exists(select *
				 from  JOURNAUX j
				 where j.type='tabloid'
				 and j.Titre not in (select A.Tite
									 from Aime A
									 where A.IdCl=C.IdCl));
