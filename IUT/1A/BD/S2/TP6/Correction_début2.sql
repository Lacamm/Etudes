DROP TABLE IF EXISTS CONSTITUER;
DROP TABLE IF EXISTS FORMULE;
DROP TABLE IF EXISTS INCOMPATIBLE;

CREATE TABLE COMPOSE (
  refcomp varchar(4),
  nomcomp varchar(20),
  PRIMARY KEY (refcomp)
);

CREATE TABLE CONSTITUER (
  idform varchar(5),
  refcomp varchar(4),
  qte decimal(5,2),
  PRIMARY KEY (refcomp, idform)
);

CREATE TABLE FORMULE (
  idform varchar(5),
  nomform varchar(15),
  PRIMARY KEY (idform)
);

CREATE TABLE INCOMPATIBLE (
  refcomp_1 varchar(4),
  refcomp_2 varchar(4),
  PRIMARY KEY (refcomp_1,refcomp_2)
);

ALTER TABLE CONSTITUER ADD FOREIGN KEY (idform) REFERENCES FORMULE (idform);
ALTER TABLE CONSTITUER ADD FOREIGN KEY (refcomp) REFERENCES COMPOSE (refcomp);
ALTER TABLE INCOMPATIBLE ADD FOREIGN KEY (refcomp_1) REFERENCES COMPOSE (refcomp);
ALTER TABLE INCOMPATIBLE ADD FOREIGN KEY (refcomp_2) REFERENCES COMPOSE (refcomp);


delimiter |
drop function if exists premier |
create function premier(liste varchar (255)) returns varchar(20)
begin
  declare res varchar(20);
  declare pos int;
  set pos = locate(',',liste ,1);
  if pos = 0 then
     set res = liste;
  else
     set res = substring(liste,1 ,pos -1);
  end if;
  return res;
end |
delimiter ;

select premier('bleu,vert,rouge,jaune');

delimiter |
drop function if exists reste |
create function reste(liste varchar(255)) returns varchar(235)
begin
  declare res varchar(235);
  declare pos int;
  set pos = LOCATE(',', liste, 1);
  if pos = 0 then
    set res= '';
  else
    set res = substring(liste, pos+1);
  end if;
  return res;
end |
  
delimiter ;

select reste('bleu,vert,rouge,jaune');
