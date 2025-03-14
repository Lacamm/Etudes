insert into Clients values ( 1, 'Dupont', 'Jean', 'Orleans');
insert into Clients values ( 2, 'Durand', 'Paul', 'Orleans');
insert into Clients values ( 3, 'Martin', 'Pierre', 'Paris');
insert into Clients values ( 4, 'Auger', 'Marcel', 'Paris');
insert into Clients values ( 5, 'Smith', 'Peter', 'Londres');
insert into Clients values ( 6, 'Barnes', 'Jane', 'Berlin');
insert into Clients values ( 7, 'Freud', 'Florian', 'Berlin');

insert into Voyages values ('V100', 'Paris', 'Amsterdam',  to_date('01-08-2013-10:30','DD-MM-YYYY-HH24:MI'), to_date('07-08-2013-14:30','DD-MM-YYYY-HH24:MI'),200.00);
insert into Voyages values ('V200', 'Paris', 'Rio de Janeiro',  to_date('01-12-2013-11:30','DD-MM-YYYY-HH24:MI'), to_date('07-12-2013-16:30','DD-MM-YYYY-HH24:MI'),2000.00);
insert into Voyages values ('V300', 'Prague', 'Amsterdam',  to_date('01-10-2013-8:30','DD-MM-YYYY-HH24:MI'), to_date('10-08-2013-15:30','DD-MM-YYYY-HH24:MI'),300.00);
insert into Voyages values ('V140', 'Paris', 'Amsterdam',  to_date('01-11-2013-10:30','DD-MM-YYYY-HH24:MI'), to_date('07-11-2013-14:30','DD-MM-YYYY-HH24:MI'),100.00);
insert into Voyages values ('V400', 'Lisbonne', 'Madrid',  to_date('01-03-2014-12:30','DD-MM-YYYY-HH24:MI'), to_date('07-03-2014-18:30','DD-MM-YYYY-HH24:MI'),400.00);
insert into Voyages values ('V500', 'Paris', 'Madrid',  to_date('01-04-2014-10:30','DD-MM-YYYY-HH24:MI'), to_date('07-04-2014-20:30','DD-MM-YYYY-HH24:MI'),300.00);
insert into Voyages values ('V600', 'Berlin', 'Madrid',  to_date('01-05-2014-10:30','DD-MM-YYYY-HH24:MI'), to_date('07-05-2014-20:30','DD-MM-YYYY-HH24:MI'),300.00);


insert into Reservations values (6, 'V100', to_date('01-07-2013-18:15','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (1, 'V100', to_date('01-06-2013-8:15','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (1, 'V200', to_date('01-05-2013-21:00','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (1, 'V400', to_date('01-11-2013-18:30','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (2, 'V400', to_date('01-11-2013-21:30','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (3, 'V140', to_date('01-06-2013-9:25','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (4, 'V300', to_date('01-05-2013-12:00','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (3, 'V100', to_date('01-05-2013-19:25','DD-MM-YYYY-HH24:MI'));
