DELIMITER |

DROP FUNCTION IF EXISTS premier;
CREATE FUNCTION premier(liste VARCHAR(255)) RETURNS VARCHAR(255)
BEGIN
    DECLARE res VARCHAR(255);
    DECLARE posFinPremierMot INT;
    SET posFinPremierMot = LOCATE(",", liste, 1);
    SET res = SUBSTRING(liste,1, posFinPremierMot - 1);
    RETURN RES;
END|


select premier('bleu,vert,rouge,jaune')|

DROP FUNCTION IF EXISTS reste;
CREATE FUNCTION reste(liste VARCHAR(255)) RETURNS VARCHAR(255)
BEGIN
    DECLARE res VARCHAR(255);
    DECLARE posFinPremierMot INT;
    SET posFinPremierMot = LOCATE(",", liste, 1);
    SET res = SUBSTRING(liste, posFinPremierMot + 1);
    RETURN RES;
END|

select reste('bleu,vert,rouge,jaune')|



DELIMITER |
drop procedure if exists test |
create procedure test(liste varchar(255))
begin
    DECLARE elem VARCHAR(30);
    DROP TABLE IF EXISTS TEST_TP6;
    CREATE TEST_TP6(elem VARCHAR(30))
    WHILE liste != ' ' do
        SET elem = premier(liste);
        INSERT INTO TEST_TP6 VALUE (elem);
        SET liste=reste(liste);
    END WHILE;
END |
call test()


-- Exo 3

DELIMITER |
drop function if exists genereEtiquette |
create function genereEtiquette(nomFormule VARCHAR(15)) returns VARCHAR(255)
begin
  declare res varchar(255) default concat(nomFormule, '');
  declare fini boolean default false;
  declare ingr varchar(20);
  declare quantite decimal(5,2);
  declare ingredients cursor for
    select nomComp, qte from FORMULE natural join CONSTITUER natural join COMPOSE
    where FORMULE.nomForm = nomFormule;
  declare continue handler for not found set fini = true;
  open ingredients;
  while not fini do
    fetch ingredients into ingr, quantite;
    if not fini then
      set res := concat(res, concat('', ingr));
      set res := concat(res, concat('(', (convert(quantite, char), ')')));
    end if;
  end while;
  close ingredients;
  return res;
end |

select genereEtiquette (Comprimés) |


-- Exo 5

delimiter |
drop table if exists HISTORIQUE|
create table HISTORIQUE( heure timestamp, action varchar(15), nomTable varchar(15), nouveau varchar(5), ancien varchar(5))|

drop trigger if exists inserer_formule|
create trigger inserer_formule after insert on FORMULE for each row
  begin insert into HISTORIQUE values(now(),'insertion ', 'FORMULE ', new.idForm ,NULL);
end|

drop trigger if exists delete_formule|
create trigger delete_formule after delete on FORMULE for each row
  begin insert into HISTORIQUE values(now(),'effacement ', 'FORMULE ',NULL, old.idForm);
end|

drop trigger if exists update_formule|
create trigger update_formule after update on FORMULE for each row begin insert into HISTORIQUE values(now(),'mise a jour', 'FORMULE ', new.idForm , old.idForm);
end|
delimiter ;

-- Exo 4
