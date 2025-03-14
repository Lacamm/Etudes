/* Exercice 1 */

/* 1 */

delimiter |

drop function if exists premier |
create function premier (liste varchar(255)) 
returns varchar(255)
begin
	if locate (',',liste,1) != 0 then 
		return substring(liste,1,locate(',',liste,1)-1);
	end if;
    return liste;
end |

delimiter ;

select premier ('bleu,rouge,jaune,vert');

/* 2 */

delimiter |

drop function if exists reste |
create function reste(liste varchar(255)) returns varchar(255)
begin
    declare res varchar(255);
    if locate(',',liste,1) = '' then 
		set res = '';
	else
		set res = substring(liste,locate(',',liste,1)+1);
	end if;
    return res;
end |

delimiter ;

select reste ('bleu,rouge,jaune,vert');

/* 3 */

delimiter |

drop table if exists TEST_TP6;
drop procedure if exists testerListe |
create procedure testerListe(liste varchar(255))
begin
	create table TEST_TP6 ( elem VARCHAR(30) ) ;
	while (length(liste)>0) do
		insert into TEST_TP6 values(premier(liste));
		set liste:= reste(liste);
	end while;
end |

delimiter ;

call testerListe('bleu,rouge,jaune,vert');


/* Exercice 2 */

/* 1 */


delimiter |

drop function if exists nbformules |
create function nbformules(nomCompose varchar(255))
returns int
begin
	declare res int;
	select count(idform) into res
	from COMPOSE natural left join CONSTITUER
	where nomcomp = nomCompose;
	return res;
end |


select nbformules('Alcool') |

/* 2 */

delimiter |

drop procedure if exists creerFormule |
create procedure creerFormule(idF int, nomF varchar(30),listeC varchar(255))
begin
	declare comp varchar(30);
	insert into FORMULE values (idF, nomF);
	while (length(listeC)>0) do
		select refcomp into comp from COMPOSE where nomcomp = premier(listeC);
		insert into CONSTITUER values(idF, comp, 1);
		set listeC:= reste(listeC);
	end while;
end |

call creerFormule(78,'lol','sucre,mercure,alcool')|

delimiter ;

/* Exercice 3 */

/* 1 */

delimiter |

drop function if exists genereEtiquette|
create function genereEtiquette(nomFormule varchar(15))
returns varchar(255)
begin

declare res varchar(255) default concat(nomFormule, ':');
declare fini int default false;
declare unIngr varchar(20);
declare quantite decimal(5,2);
declare ingredients cursor for 
select nomComp, qte from FORMULE F natural join CONSTITUER natural join COMPOSE
where F.nomForm = nomFormule;
declare continue handler for not found set fini = true;

open ingredients;
while not fini do
	fetch ingredients into unIngr, quantite;
	if not fini then
		set res = contact(res, concat(' ', unIngr));
		set res = contact(res, concat('(', concat(convert(quantite, char),')')));
	end if;
end while;
close ingredients;

return res;
end |

delimiter ;


/* Exercice 4 */

/* 1) */

delimiter |

drop procedure if exists completeIncompatible|
create procedure completeIncompatible()
begin
declare fini int default false;
declare ref1, ref2 varchar(4);
declare nb int;

declare lesIncomp cursor for select refcomp_1, refcomp_2 from INCOMPATIBLE;
declare continue handler for not found set fini=true;

open lesIncomp;
while not fini do
fetch lesIncomp into ref1, ref2;
if not fini then
	select count(*) into nb
	from INCOMPATIBLE where refcomp_1=ref2 and refcomp_2=ref1;
	if nb = 0 then
	insert into INCOMPATIBLE values(ref2,ref1);
	end if;
end if;
end while;
close LesIncomp;

end|

delimiter ;


/* Exercie 5 */

/* 1) */

delimiter |

drop trigger if exists inserer_formule|
create trigger inserer_formule after insert on FORMULE for each row 
begin 
	insert  into HISTORIQUE values(now(),'insertion', 'FORMULE', new.idForm ,NULL);
end|

drop trigger  if exists  delete_formule|
create trigger delete_formule after delete on FORMULE for each row
begin 
	insert into HISTORIQUE values(now(),'effacement', 'FORMULE', NULL, old.idForm);
end|


drop trigger if exists update_formule|
create trigger update_formule after update on FORMULE for each  row 
begin
insert into HISTORIQUE values(now(),'mise à jour', 'FORMULE', new.idForm , old.idForm);
end|


delimiter ;

/*  2) */


/* select count(*)
from  CONSTITUER C2, INCOMPATIBLE I
where C2.idform = new.idform
and I.refcomp_1 = new.refcomp and I.refcomp_2 = C2.refcomp
*/




























































