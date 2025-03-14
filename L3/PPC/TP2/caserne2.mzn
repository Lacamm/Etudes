include "pompier.dzn";

% servi[c,v] = 1, si caserne en ville c sert ville v, 0 sinon
array [1..nVille] of var 0..1 : caserne;
array [1..nVille] of var 0..nVille : acs;


% chaque ville est à moins de 15 minutes de la caserne qui sert la ville 
constraint forall(v in 1..nVille) (duree[acs[v],v]<=15);

% une caserne qui sert une ville doit etre ouverte
constraint forall(v in 1..nVille) (caserne[acs[v]]=1);

% chaque ville est servie par une caserne
% exprimer par l'instanciation de la variable

% une ville qui a une caserne ouverte est servie par elle meme
constraint forall(v in 1..nVille) (caserne[v]=1 -> acs[v]=v);
              

solve minimize sum(caserne);