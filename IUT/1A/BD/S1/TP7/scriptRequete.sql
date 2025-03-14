-- @ SCRIPTS/requetesVOYAGES

select VilleArrivee from VOYAGES where VilleDepart='PAris';
select * from VOYAGES where VilleArrivee='Amsterdam';
select VilleDepart, to_char(Depart, 'DD-MM-YYYY-HH24:mi')Depart from VOYAGES where VilleArrivee='Amsterdam';
select Nom, VilleArrivee, Prix from CLIENTS natural join RESERVATIONS natural join VOYAGES order by Nom, Prix DESC;
select Nom, VilleDepart, Code from CLIENTS natural join RESERVATIONS natural join VOYAGES where Ville = VilleDepart;

--
select VilleDepart, VilleArrivee, to_char(Depart, 'DD-MM-YYYY-HH24:mi')Depart from VOYAGES where (Depart-Sysdate)>3 order by Depart; 
select Ville from CLIENTS natural join RESERVATIONS natural join VOYAGES where Ville=VilleArrivee or Ville=VilleDepart;
select Nom, Prenom from CLIENTS where Ville!='Paris';
select Nom, Prenom from CLIENTS natural join RESERVATIONS natural join VOYAGES where Ville!='Paris' and VilleDepart='Paris';

select Id from CLIENTS minus select Id from RESERVATIONS;
select Code from VOYAGES minus select Code from RESERVATIONS;
select distinct Nom from CLIENTS natural join RESERVATIONS natural join VOYAGES where VilleArrivee='Amsterdam' and VilleDepart='Paris' minus select distinct Nom from CLIENTS natural join RESERVATIONS natural join VOYAGES where VilleArrivee!='Amsterdam' and VilleDepart='Paris';
select Nom, Prenom from CLIENTS natural join RESERVATIONS natural join VOYAGES where VilleArrivee='Amsterdam' intersect select Nom, Prenom from CLIENTS natural join RESERVATIONS natural join VOYAGES where VilleArrivee='Rio de Janeiro';
select Nom, Prenom from CLIENTS natural join RESERVATIONS natural join VOYAGES where VilleArrivee='Amsterdam' or VilleArrivee='Rio de Janeiro';

select C1.Nom, C1.Prenom, C2.Nom, C2.Prenom, C1.Ville from CLIENTS C1, CLIENTS C2 where C1.Ville=C2.Ville and C1.Id<C2.Id;
select V1.Code, V2.Code, V1.Prix from VOYAGES V1, VOYAGES V2 where V1.Code<V2.Code and V1.Prix=V2.Prix;

