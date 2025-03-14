-- Devoir 103
-- Nom: ALLAIN , Prenom: Lucas

-- Devoir sur machine 1
-- dur�e 1 heure
-- On rappelle que la fonction YEAR(date) retourne l'ann�e d'une date
-- 
-- Veillez � bien r�pondre aux emplacements indiqu�s.
-- Seule la premi�re requ�te est prise en compte.

-- +-----------------------+--
-- * Question 103497 : 2pts --
-- +-----------------------+--
-- Ecrire une requ�te qui renvoie les informations suivantes:
--  Quels sont les sond�s du panel France Global 1 qui se pr�nomment L�a?

-- Voici le d�but de ce que vous devez obtenir.
-- ATTENTION � l'ordre des colonnes et leur nom!
-- +---------+-----------+------------+
-- | numSond | nomSond   | prenomSond |
-- +---------+-----------+------------+
-- | 36      | MABIKIN   | L�a        |
-- | 40      | CHAUSS    | L�a        |
-- | 210     | GODRR     | L�a        |
-- | 242     | BAIG      | L�a        |
-- | 554     | CONE      | L�a        |
-- | 556     | CHEGEARD  | L�a        |
-- | 560     | DUPART    | L�a        |
-- | 596     | POULBO    | L�a        |
-- | 624     | BAROIEIER | L�a        |
-- | 682     | DAILIELT  | L�a        |
-- | etc...
-- = Reponse question 103497.

select numSond,nomSond, prenomSond
from SONDE 
where numSond in(
	select numSond
	from SONDE natural join CONSTITUER natural join PANEL
	where nomPan= 'France Global 1' and prenomSond = 'Lea');


-- +-----------------------+--
-- * Question 103521 : 2pts --
-- +-----------------------+--
-- Ecrire une requ�te qui renvoie les informations suivantes:
--  Quelles sont les tranches d'age qui ne comportent aucun sond� nomm� Osman?

-- Voici le d�but de ce que vous devez obtenir.
-- ATTENTION � l'ordre des colonnes et leur nom!
-- +------+----------+--------+
-- | idTR | valDebut | valFin |
-- +------+----------+--------+
-- | 1    | 20       | 29     |
-- | 3    | 40       | 49     |
-- | 4    | 50       | 59     |
-- | 5    | 60       | 69     |
-- | 6    | 70       | 120    |
-- +------+----------+--------+
-- = Reponse question 103521.

select idTR, valdebut, valFin
from TRANCHE
where idTR not in(
	select idTR
	from TRANCHE natural join CARACTERISTIQUE natural join SONDE
	where prenomSond='Osman');


-- +-----------------------+--
-- * Question 103565 : 2pts --
-- +-----------------------+--
-- Ecrire une requ�te qui renvoie les informations suivantes:
--  Quel est le nombre de femmes par tranche d'�ge?

-- Voici le d�but de ce que vous devez obtenir.
-- ATTENTION � l'ordre des colonnes et leur nom!
-- +------+----------+--------+----------+
-- | idTR | valDebut | valFin | nbFemmes |
-- +------+----------+--------+----------+
-- | 1    | 20       | 29     | 94       |
-- | 2    | 30       | 39     | 117      |
-- | 3    | 40       | 49     | 113      |
-- | 4    | 50       | 59     | 115      |
-- | 5    | 60       | 69     | 102      |
-- | 6    | 70       | 120    | 133      |
-- +------+----------+--------+----------+
-- = Reponse question 103565.

select idTR, valDebut, valFin, count(numSond) as nbFemmes
from TRANCHE natural join CARACTERISTIQUE natural join SONDE
where sexe = 'F'
group by idTR;

-- +-----------------------+--
-- * Question 103598 : 2pts --
-- +-----------------------+--
-- Ecrire une requ�te qui renvoie les informations suivantes:
--  Quelle sont les tranches d'�ge qui contiennent plus de 4 personnes appel�es Camille?

-- Voici le d�but de ce que vous devez obtenir.
-- ATTENTION � l'ordre des colonnes et leur nom!
-- +------+----------+--------+-----------+
-- | idTR | valDebut | valFin | nbCamille |
-- +------+----------+--------+-----------+
-- | 5    | 60       | 69     | 5         |
-- | 6    | 70       | 120    | 6         |
-- +------+----------+--------+-----------+
-- = Reponse question 103598.

select distinct idTR, valDebut, valFin, count(numSond) as nbCamille
from TRANCHE natural join CARACTERISTIQUE natural join SONDE
where prenomSond = 'Camille'
group by idTR
having count(numSond) > 4;


-- +-----------------------+--
-- * Question 103600 : 2pts --
-- +-----------------------+--
-- Ecrire une requ�te qui renvoie les informations suivantes:
--  Quelles sont les cat�gories dont tous les sond�s n�s en 1978 sont des femmes? (on consid�re que les cat�gories qui n'ont aucun sond� n� en 1978 font partie de la r�ponse) 

-- Voici le d�but de ce que vous devez obtenir.
-- ATTENTION � l'ordre des colonnes et leur nom!
-- +-------+--------------------------------+
-- | idcat | intitulecat                    |
-- +-------+--------------------------------+
-- | 3     | Cadres, professions intellectu |
-- | 7     | Inactifs ayant d�j� travaill�  |
-- | 8     | Autres sans activit� professio |
-- +-------+--------------------------------+
-- = Reponse question 103600.

select distinct idCat,intituleCat
from CATEGORIE 
where idCat not in(
	select idCat
	from CATEGORIE natural join CARACTERISTIQUE natural join SONDE 
	where YEAR(dateNaisSond)=1978 and sexe!='F');

