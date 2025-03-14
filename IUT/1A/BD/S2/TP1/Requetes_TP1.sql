-- @ SrequetesTP1

-- 1
select nomPan
from PANEL natural join CONSTITUER natural join SONDE
where nomSond = 'BOURIER' and prenomSond = 'Caroline';

select nomPan 
from PANEL p join CONSTITUER c on p.idPan = c.idPan join SONDE s on c.numSond = s.numSond
where s.nomSond = 'BOURIER' and s.prenomSond = 'Caroline';

select nomPan from PANEL p
where idPan in(
select idPan from CONSTITUER
where numSond in (
select numSond from SONDE s
where s.nomSond = 'BOURIER' and s.prenomSond = 'Caroline'
)
);

select nomPan from PANEL p
where exists(
select 1 from CONSTITUER c where p.idPan = c.idPan
and exists(
select 1 from SONDE s
where nomSond = 'BOURIER' and prenomSond = 'Caroline'
and s.numSond = c.numSond)
);

-- 2
select distinct nompan
from PANEL natural join SONDE natural join TRANCHE natural join CARACTERISTIQUE natural join CONSTITUER
where valdebut = 70 and valfin = 120; 

-- 5
select distinct valdebut, valfin
from SONDE natural join CARACTERISTIQUE natural join TRANCHE
where sexe = 'F' and DAY(datenaissond) = 25 and MONTH(datenaissond) = 4;


-- 6
select distinct prenomSond, nomSond
from SONDE natural join CONSTITUER as c1 ,CONSTITUER as c2
where prenomSond = 'Jean' and c1.numsond = c2.numsond and c1.idpan<>c2.idpan;

