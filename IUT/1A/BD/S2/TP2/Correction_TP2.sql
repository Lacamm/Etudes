-- TP 2
-- Nom: DOLPHIN , Prenom: Nicolas

-- +------------------+--
-- * Question 1 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les panels dont ne fait pas partie Louane DJARA?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------------+
-- | nomPan          |
-- +-----------------+
-- | France global 1 |
-- | Moins de 50 ans |
-- +-----------------+
-- = Reponse question 1.
select nompan from PANEL where idPan not IN (select idPan from CONSTITUER natural join SONDE where nomsond = 'DJARA' and prenomsond = 'Louane');

-- +------------------+--
-- * Question 2 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les prénoms de sondé commençant par un A qui n'apparaissent pas dans la tranche d'age 20-29 ans? Classez ces noms par ordre alphabétique.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +------------+
-- | prenomSond |
-- +------------+
-- | Alice      |
-- | Allan      |
-- | Amaury     |
-- | Ambre      |
-- | Anaïs      |
-- | etc...
-- = Reponse question 2.
select distinct prenomSond from SONDE where prenomSond like "A%" and prenomSond not in (select prenomSond from SONDE natural join CARACTERISTIQUE natural join TRANCHE where valDebut = 20 and valFin = 29) order by prenomSond;


-- +------------------+--
-- * Question 3 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--   Quels sont les panels dont tous les sondés ont moins de 60 ans? Rappel: CURDATE() donne la date du jour et DATEDIFF(d1,d2) donne le nombre de jours entre d1 et d2.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------------+
-- | nomPan          |
-- +-----------------+
-- | Moins de 50 ans |
-- +-----------------+
-- = Reponse question 3.
select distinct nompan  from PANEL where idPan not in(select idPan from CONSTITUER natural join SONDE where DATEDIFF(CURDATE(), dateNaisSond) >= 60*365);


-- +------------------+--
-- * Question 4 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quelles sont les catégories qui comportent des personnes nées en 1974? On rappelle que YEAR(d) donne l'année de la date d sous la forme d'un entier.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +--------------------------------+
-- | intituleCat                    |
-- +--------------------------------+
-- | Cadres, professions intellectu |
-- | Professions intermédiaires     |
-- | Employés                       |
-- | Ouvriers                       |
-- | Inactifs ayant déjà travaillé  |
-- +--------------------------------+
-- = Reponse question 4.
select intitulecat from CATEGORIE where idCat in(select idCat from CARACTERISTIQUE natural join SONDE where YEAR(datenaissond) = 1974);


-- +------------------+--
-- * Question 5 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--   Quels sont les sondés nés en 1997 qui appartiennent aux panels France global 1 et France global 2?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------+------------+
-- | nomSond   | prenomSond |
-- +-----------+------------+
-- | DOILELTIS | Nina       |
-- +-----------+------------+
-- = Reponse question 5.
select nomSond , prenomSond from SONDE where YEAR(dateNaisSond) = 1997 and numSond in (select c1.numSond from CONSTITUER c1 natural join PANEL p1, CONSTITUER c2 natural join PANEL p2 where p1.nomPan = "France global 1" and p2.nomPan = "France global 2" and c1.numSond = c2.numSond);


-- +------------------+--
-- * Question 6 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les sondés nés en 1974 qui ont la même date de naissance?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +---------+------------+----------+------------+
-- | nomSond | prenomSond | nomSond  | prenomSond |
-- +---------+------------+----------+------------+
-- | DASA    | Maxime     | PEKARDAC | Bilal      |
-- +---------+------------+----------+------------+
-- = Reponse question 6.
select s1.nomSond , s1.prenomSond, s2.nomSond, s2.prenomSond from SONDE s1, SONDE s2 where YEAR(s1.dateNaisSond) = 1974 and s1.dateNaisSond = s2.dateNaisSond and s1.numSond > s2.numSond;


