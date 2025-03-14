delimiter |
drop function if exists premier |

create function premier(liste varchar(255)) returns varchar(20)
begin
    declare res varchar(20);
    declare i int default 1;
    set res = substring(liste,1,locate(',',liste,i)-1);
    return res;
end |



drop function if exists reste |

create function reste(liste varchar(255)) returns varchar(255)
begin
    declare res varchar(255);
    set res = substring(liste,locate(',',liste,1)+1,length(liste));
    return res;
end |


drop function if exists nbFormules |

create function nbFormules(nomCompose varchar(20)) returns int
begin
    
end