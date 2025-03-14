include "pompier.dzn";

% servi[c,v] = 1, si caserne en ville c sert ville v, 0 sinon
array [1..nVille] of var 0..1 : caserne;
array [1..nVille, 1..nVille] of var 0..1 : servi;


% chaque ville est à moins de 15 minutes de la caserne qui sert la ville 
constraint forall(c in 1..nVille, v in 1..nVille) (duree[c,v] * servi[c,v] <= 15);
% servi[c,v]=1 -> duree[c,v]<=15

% une caserne qui sert une ville doit etre ouverte
constraint forall(c,v in 1..nVille) (caserne[c] >= servi[c,v]);

% chaque ville est servie par une caserne
constraint forall(c,v in 1..nVille) (sum([servi[c,v] | c in 1..nVille])=1);

% une ville qui a une caserne ouverte est servie par elle meme
constraint forall(c in 1..nVille) (caserne[c]=servi[c,c]);
              

solve minimize sum(caserne);