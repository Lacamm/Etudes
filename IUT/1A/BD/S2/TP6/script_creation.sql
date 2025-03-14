DROP TABLE IF EXISTS FORMULE;
DROP TABLE IF EXISTS COMPOSE;
DROP TABLE IF EXISTS CONSTITUER;
DROP TABLE IF EXISTS INCOMPATIBLE;

CREATE TABLE COMPOSE (
refcomp varchar (4) ,
nomcomp varchar (20) ,
PRIMARY KEY ( refcomp )
);

CREATE TABLE CONSTITUER (
idform varchar (5) ,
refcomp varchar (4) ,
qte decimal (5 ,2) ,
PRIMARY KEY ( refcomp , idform )
);

CREATE TABLE FORMULE (
idform varchar (5) ,
nomform varchar (15) ,
PRIMARY KEY ( idform )
);

CREATE TABLE INCOMPATIBLE (
refcomp_1 varchar (4) ,
refcomp_2 varchar (4) ,
PRIMARY KEY ( refcomp_1 , refcomp_2 )
);




ALTER TABLE CONSTITUER ADD FOREIGN KEY ( idform ) REFERENCES FORMULE ( idform ) ;
ALTER TABLE CONSTITUER ADD FOREIGN KEY ( refcomp ) REFERENCES COMPOSE ( refcomp ) ;
ALTER TABLE INCOMPATIBLE ADD FOREIGN KEY ( refcomp_1 ) REFERENCES COMPOSE ( refcomp ) ;
ALTER TABLE INCOMPATIBLE ADD FOREIGN KEY ( refcomp_2 ) REFERENCES COMPOSE ( refcomp ) ;
