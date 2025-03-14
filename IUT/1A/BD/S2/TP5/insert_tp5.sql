/* Jean Dupont */
insert into LIEU values (1,"Orléans");
insert into CLUB values (1,'USO',"Union Sportive d'Orléans");
insert into CATEGORIE values (1,"Senior");
insert into COUREUR values (1, "Dupont", "Jean", 1, 1);
insert into EVENEMENT values (1, "Foulees d’Orleans", STR_TO_DATE('12/12/2015','%d/%m/%Y'), 1);
insert into COURSE values (1,STR_TO_DATE('09:00', '%h:%i'),1,1);
insert into EFFECTUER values (STR_TO_DATE('12:32', '%i:%s'), 1, 1, 1);

/* Marie Duval */

insert into LIEU values (2,"Olivet");
insert into CLUB values (2,'ASM',"Association Sportive de Marville");
insert into CATEGORIE values (2,"Junior");
insert into COUREUR values (2, "Duval", "Marie Junior", 2, 2);
insert into EVENEMENT values (2, "Corrida d'Olivet", STR_TO_DATE('25/12/2015','%d/%m/%Y'), 2);
insert into COURSE values (2,STR_TO_DATE('11:00', '%h:%i'),2,2);
insert into EFFECTUER values (STR_TO_DATE('11:53', '%i:%s'),2,2,2);

/* Vite-Tours */

insert into LIEU values(3, "Tours");
insert into EVENEMENT values (3, "Vite-Tours", STR_TO_DATE('18/03/2016', '%d/%m/%Y'), 3);
insert into COURSE values
	(3, STR_TO_DATE('09:00', '%h:%i'),3,1),
    (3, STR_TO_DATE('10:30', '%h:%i'),3,2);  

--Delete from CLUB where sigleCL = "USO";
-- Ca supprime une clé primaire
