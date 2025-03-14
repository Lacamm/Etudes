
/* Destinations from Paris*/

select VilleArrivee from VOYAGES where VilleDepart='Paris';

/* Clients to Amsterdam */

select Id from RESERVATIONS natural join VOYAGES where VilleArrivee='Amsterdam';


