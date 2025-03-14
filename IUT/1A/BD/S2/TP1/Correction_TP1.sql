-- TP 1
-- Nom: DECAUX  , Prenom: Julie

-- +------------------+--
-- * Question 1 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Donner la liste des panels dont fait partie Caroline BOURIER.

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------------+
-- | nomPan          |
-- +-----------------+
-- | France global 1 |
-- +-----------------+
-- = Reponse question 1.
select nompan
from PANEL natural join SONDE natural join CONSTITUER
where nomsond = 'BOURIER' and prenomsond = 'Caroline';

select nompan
from PANEL
  where idPan IN (
  select idPan
  from CONSTITUER natural join SONDE
  where nomsond = 'BOURIER' and prenomsond = 'Caroline');

select nompan
from PANEL p
where EXISTS (
  select *
  from CONSTITUER c natural join SONDE
  where p.idPan = c.idPan and nomsond = 'BOURIER' and prenomsond = 'Caroline');

-- +------------------+--
-- * Question 2 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les panels dont un des sondés est de la tranche d'âge 70 à 120 ans?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------------+
-- | nomPan          |
-- +-----------------+
-- | France global 1 |
-- | France global 2 |
-- +-----------------+
-- = Reponse question 2.
select distinct nompan
from PANEL natural join SONDE natural join TRANCHE natural join CARACTERISTIQUE natural join CONSTITUER
where valdebut = 70 and valfin = 120;

select nompan
from PANEL
where idPan IN (
  select idPan
  from SONDE natural join TRANCHE natural join CARACTERISTIQUE natural join CONSTITUER
  where valdebut = 70 and valfin = 120);

select nompan
from PANEL p
where EXISTS (
  select *
  from SONDE natural join TRANCHE natural join CARACTERISTIQUE natural join CONSTITUER c
  where p.idPan = c.idPan and valdebut = 70 and valfin = 120);
-- +------------------+--
-- * Question 3 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les sondés de la tranche d'age 70-120 ans qui sont ouvriers?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------+------------+
-- | nomSond   | prenomSond |
-- +-----------+------------+
-- | ERYS      | Imane      |
-- | BERRGAIES | Claire     |
-- | JABAT     | Rose       |
-- | WALLOCHE  | Marion     |
-- | LENUJA    | Pauline    |
-- | etc...
-- = Reponse question 3.

select nomsond, prenomsond
from SONDE natural join TRANCHE natural join CARACTERISTIQUE natural join CATEGORIE
where valdebut = 70 and valfin = 120 and intitulecat = 'ouvriers';

select nomsond, prenomsond
from SONDE where idc IN (
  select idc
  from TRANCHE natural join CARACTERISTIQUE c natural join CATEGORIE
  where valdebut = 70 and valfin = 120 and intitulecat = 'ouvriers');

select nomsond, prenomsond
from SONDE s
where EXISTS (
  select *
  from TRANCHE natural join CARACTERISTIQUE c natural join CATEGORIE
  where s.idc = c.idc and valdebut = 70 and valfin = 120 and intitulecat = 'ouvriers');

-- +------------------+--
-- * Question 4 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les ouvriers qui portent le prénom Olivier?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +-----------+------------+
-- | nomSond   | prenomSond |
-- +-----------+------------+
-- | THALOUERD | Olivier    |
-- | POTRININ  | Olivier    |
-- +-----------+------------+
-- = Reponse question 4.
select nomsond, prenomsond
from SONDE natural join CARACTERISTIQUE natural join CATEGORIE
where prenomsond = 'Olivier' and intitulecat = 'ouvriers';

select nomsond, prenomsond
from SONDE
where idc IN (
  select idc
  from  CARACTERISTIQUE c natural join CATEGORIE
  where  prenomsond = 'Olivier' and intitulecat = 'ouvriers');

select nomsond, prenomsond
from SONDE s
where EXISTS (
  select *
  from  CARACTERISTIQUE c natural join CATEGORIE
  where s.idc = c.idc and prenomsond = 'Olivier' and intitulecat = 'ouvriers');

-- +------------------+--
-- * Question 5 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les tranches d'âge qui comportent une ou plusieurs femmes nées un 25 avril?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +----------+--------+
-- | valDebut | valFin |
-- +----------+--------+
-- | 40       | 49     |
-- +----------+--------+
-- = Reponse question 5.
select distinct valdebut, valfin
from SONDE natural join CARACTERISTIQUE natural join TRANCHE
where sexe = 'F' and DAY(datenaissond) = 25 and MONTH(datenaissond) = 4;

select valdebut, valfin
from TRANCHE where idtr IN (
  select idtr
  from SONDE natural join CARACTERISTIQUE
  where sexe = 'F' and DAY(datenaissond) = 25 and MONTH(datenaissond) = 4);

select valdebut, valfin
from TRANCHE t
where EXISTS (
  select *
  from SONDE natural join CARACTERISTIQUE c
  where t.idtr = c.idtr and sexe = 'F' and DAY(datenaissond) = 25 and MONTH(datenaissond) = 4);

-- +------------------+--
-- * Question 6 :     --
-- +------------------+--
-- Ecrire une requête qui renvoie les informations suivantes:
--  Quels sont les sondés prénommés Jean qui appartiennent à au moins 2 panels différents?

-- Voici le début de ce que vous devez obtenir.
-- ATTENTION à l'ordre des colonnes et leur nom!
-- +------------+----------+
-- | prenomSond | nomSond  |
-- +------------+----------+
-- | Jean       | DILY     |
-- | Jean       | JATECHU  |
-- | Jean       | PIETIENE |
-- | Jean       | FAL      |
-- | Jean       | BOYEGHE  |
-- +------------+----------+
-- = Reponse question 6.
select distinct prenomSond, nomSond
from SONDE natural join CONSTITUER as c1 ,CONSTITUER as c2
where prenomSond = 'Jean' and c1.numsond = c2.numsond and c1.idpan<>c2.idpan;
