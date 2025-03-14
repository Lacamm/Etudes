/* insert into COMPOSE values ('Me01','Mercure'), ('Al01','Alcool'),('Ox01','Oxygène'), ('Di01','Dioxyde de soufre'), ('Di02','Dioxyde d''oxygène'), ('Su01','Sucre');
insert into INCOMPATIBLE values ('Me01','Al01'), ('Me01','Ox01');
insert into FORMULE values ('Po001','Pommade'), ('Co001', 'Comprimés');
insert into CONSTITUER values ('Po001','Al01',1.2), ('Po001','Di01',0.5),('Co001', 'Di01',0.01),('Co001','Su01',5.3), ('Co001','Di02',1.2); 
*/
drop table if exists HISTORIQUE
create table HISTORIQUE( heure timestamp, action  varchar(15), nomTable varchar(15),nouveau varchar(5), ancien varchar(5))|

insert  into FORMULE values('XX001', 'XXXXXX');
insert  into FORMULE values('YY001', 'YYYYYY');
update FORMULE set idForm ='XX002' where idForm ='YY001';
delete  from FORMULE where idForm like 'XX%' ;
