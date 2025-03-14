-- @ SCRIPTS/instanceJOURNAUX;

insert into Journaux values ('Le Canard', 'tabloid', 'satirique', 1.20);
insert into Journaux values ('Charlie Hebdo', 'tabloid', 'satirique', 3.00);
insert into Journaux values ('Le Point', 'magazine', 'actualite', 4.00);
insert into Journaux values ('Nouvel Observateur', 'magazine', 'actualite', 4.00);
insert into Journaux values ('Maison et travaux', 'magazine', 'decoration', 5.00);
insert into Journaux values ('Science et Vie', 'magazine', 'science', 5.00);
insert into Journaux values ('Pour la Science', 'magazine', 'science', 5.00);

insert into Kiosques values ('Le progress', 'Paris', 'Alesia');
insert into Kiosques values ('Liberte', 'Paris', 'Montmartre');
insert into Kiosques values ('Jussieu', 'Paris', 'Jussieu');
insert into Kiosques values ('Republique', 'Paris', 'Jussieu');
insert into Kiosques values ('Les Champs', 'Paris', 'C. Elysees');
insert into Kiosques values ('Liberte', 'Orleans', 'Martroi');
insert into Kiosques values ('Jeanne', 'Orleans', 'Dunois');
insert into Kiosques values ('La republique', 'Orleans', 'Republique');
insert into Kiosques values ('Liberte', 'Blois', 'Gare');
insert into Kiosques values ('Liberte', 'Orsay', 'Gare');

insert into Vend values ('Liberte', 'Orsay', 'Le Canard');
insert into Vend values ('Liberte', 'Orsay', 'Le Point');
insert into Vend values ('Liberte', 'Orsay', 'Nouvel Observateur');
insert into Vend values ('Liberte', 'Orsay', 'Charlie Hebdo');

insert into Vend values ('Liberte', 'Orleans', 'Le Canard');
insert into Vend values ('Liberte', 'Orleans', 'Le Point');
insert into Vend values ('Liberte', 'Orleans', 'Nouvel Observateur');
insert into Vend values ('Liberte', 'Orleans', 'Science et Vie');

insert into Vend values ('Jeanne', 'Orleans', 'Le Canard');
insert into Vend values ('Jeanne', 'Orleans', 'Le Point');
insert into Vend values ('Jeanne', 'Orleans', 'Nouvel Observateur');
insert into Vend values ('Jeanne', 'Orleans', 'Maison et travaux');
insert into Vend values ('Jeanne', 'Orleans', 'Science et Vie');

insert into Vend values ('La Republique', 'Orleans', 'Le Canard');
insert into Vend values ('La Republique', 'Orleans', 'Le Point');
insert into Vend values ('La Republique', 'Orleans', 'Nouvel Observateur');
insert into Vend values ('La Republique', 'Orleans', 'Maison et travaux');



insert into Vend values ('Liberte', 'Blois', 'Le Canard');
insert into Vend values ('Liberte', 'Blois', 'Le Point');

insert into Vend values ('Liberte', 'Paris', 'Le Canard');
insert into Vend values ('Liberte', 'Paris', 'Le Point');
insert into Vend values ('Liberte', 'Paris', 'Pour la Science');

insert into Vend values ('Jussieu', 'Paris', 'Le Canard');
insert into Vend values ('Jussieu', 'Paris', 'Le Point');
insert into Vend values ('Jussieu', 'Paris', 'Pour la Science');
insert into Vend values ('Jussieu', 'Paris', 'Maison et travaux');

insert into Vend values ('Les Champs', 'Paris', 'Le Canard');
insert into Vend values ('Les Champs', 'Paris', 'Le Point');
insert into Vend values ('Les Champs', 'Paris', 'Pour la Science');
insert into Vend values ('Les Champs', 'Paris', 'Maison et travaux');
insert into Vend values ('Les Champs', 'Paris', 'Charlie Hebdo');

--Test NULL - USE WHEN NEEDED
--insert into Clients values(100, null, null, null);
--insert into Clients values(200, null, null, null);
--insert into Clients values(201, 'toto', null, null);
--insert into Clients values(300, 'aa', 20, null);
--insert into Clients values(400, 'aa', 20, null);
--insert into Clients values(500, 'aa', 20, 'f');
--insert into Clients values(600, 'aa', null, 'm');
---

insert into Clients values(1, 'Matos', 40, 'M');
insert into Clients values(2, 'Dupont', 45, 'M');
insert into Clients values(3, 'Pereira', 30, 'M');
insert into Clients values(4, 'Dubois', 18, 'M');
insert into Clients values(5, 'Martin', 25, 'M');

insert into Clients values(6, 'Vidigal', 40, 'F');
insert into Clients values(7, 'Alves', 44, 'F');
insert into Clients values(8, 'Ferrari', 35, 'F');
insert into Clients values(9,  'Dumont', 19, 'F');
insert into Clients values(10,'Leblanc', 25, 'F');
insert into Clients values(11, 'Martin', 25, 'F');

insert into Aime values (8, 'Le Canard'); 
insert into Aime values (9, 'Le Canard'); 
insert into Aime values (10, 'Le Canard'); 
insert into Aime values (1, 'Le Canard'); 
insert into Aime values (2, 'Le Canard'); 
insert into Aime values (3, 'Le Canard'); 
insert into Aime values (3, 'Charlie Hebdo');
insert into Aime values (8, 'Charlie Hebdo');  
insert into Aime values (4, 'Charlie Hebdo');  
insert into Aime values (5, 'Charlie Hebdo');  
insert into Aime values (8, 'Nouvel Observateur'); 
insert into Aime values (1, 'Nouvel Observateur'); 
insert into Aime values (2, 'Nouvel Observateur'); 
insert into Aime values (9, 'Nouvel Observateur'); 

insert into Achat_Habituel values (9, 'Nouvel Observateur', 'La Republique', 'Orleans'); 
insert into Achat_Habituel values (3, 'Nouvel Observateur', 'La Republique', 'Orleans'); 
insert into Achat_Habituel values (3, 'Le Point', 'La Republique', 'Orleans'); 
insert into Achat_Habituel values (1, 'Le Canard','Liberte', 'Orsay');
insert into Achat_Habituel values (1, 'Charlie Hebdo','Liberte', 'Orsay');
insert into Achat_Habituel values (2, 'Le Canard','Liberte', 'Orsay');
insert into Achat_Habituel values (2, 'Charlie Hedbo','Liberte', 'Orsay');
insert into Achat_Habituel values (1, 'Maison et travaux','Liberte', 'Orsay');
