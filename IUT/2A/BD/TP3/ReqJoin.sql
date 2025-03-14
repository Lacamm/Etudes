spool resOptiJoinReq.txt;

set linesize 500

set autotrace traceonly explain statistics;

--B1)
alter session set OPTIMIZER_MODE=ALL_ROWS;

alter system flush buffer_cache;
select titre, nom
from HALFELD.FILM1 f, HALFELD.ARTISTE a
where codepays = 'aaej' and f.idmes=a.idartiste;

alter session set OPTIMIZER_MODE=RULE;
alter system flush buffer_cache;
select titre, nom
from HALFELD.FILM2 f, HALFELD.ARTISTE a
where codepays = 'aaej' and f.idmes=a.idartiste;

alter system flush buffer_cache;
select titre, nom
from HALFELD.FILM3 f, HALFELD.ARTISTE a
where codepays = 'aaej' and f.idmes=a.idartiste;

alter system flush buffer_cache;
select titre, nom
from HALFELD.FILM5 f, HALFELD.ARTISTE a
where codepays = 'aaej' and f.idmes=a.idartiste;

 
 
 

 --B1)
alter session set OPTIMIZER_MODE=FIRST_ROWS;

alter system flush buffer_cache;
select titre, nom
from HALFELD.FILM1 f, HALFELD.ARTISTE a
where codepays = 'aaej' and f.idmes=a.idartiste;

alter session set OPTIMIZER_MODE=RULE;
alter system flush buffer_cache;
select titre, nom
from HALFELD.FILM2 f, HALFELD.ARTISTE a
where codepays = 'aaej' and f.idmes=a.idartiste;


alter system flush buffer_cache;
select titre, nom
from HALFELD.FILM3 f, HALFELD.ARTISTE a
where codepays = 'aaej' and f.idmes=a.idartiste;

alter system flush buffer_cache;
select titre, nom
from HALFELD.FILM5 f, HALFELD.ARTISTE a
where codepays = 'aaej' and f.idmes=a.idartiste;
