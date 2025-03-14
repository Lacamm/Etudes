spool resCondAnnee.txt;

set linesize 500

set autotrace traceonly explain statistics;


--QUERY condition annee
alter session set OPTIMIZER_MODE=ALL_ROWS;
alter system flush buffer_cache;
select SQL_NO_CACHE annee, TITRE from HALFELD.FILM2 where annee=1999;

alter system flush buffer_cache;
select titre from HALFELD.FILM3 where annee=1999;

alter system flush buffer_cache;
select titre from HALFELD.FILM4 where annee=1999;

alter system flush buffer_cache;
select titre from HALFELD.FILM5 where annee=1999;
 
 
 
 --QUERY condition annee
alter session set OPTIMIZER_MODE=FIRST_ROWS;
alter system flush buffer_cache;

select titre from HALFELD.FILM2 where annee=1999;
alter system flush buffer_cache;

select titre from HALFELD.FILM3 where annee=1999;
alter system flush buffer_cache;

select titre from HALFELD.FILM4 where annee=1999;
alter system flush buffer_cache;

select titre from HALFELD.FILM5 where annee=1999;

spool off;
