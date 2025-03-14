select idO,nomO,descrip
from PROFIL natural join COMPORTE natural join UTILISATEUR natural join OBJET natural join VENTE  
where datefin>CURDATE() and pseudo='iuto';

select idM,contenuMessage,dateM,heureM
from MESSAGES natural join UTILISATEUR natural join PROFIL natural join COMPORTE
where pseudo='iuto' and messagelu='0';

select count(idAcquereur) as nbAchats
from VENTE natural join PROPOSITION natural join UTILISATEUR natural join PROFIL natural join COMPORTE
where pseudo='iuto' and idU=idAcquereur;
