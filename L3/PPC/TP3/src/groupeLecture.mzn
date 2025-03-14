int: N=10;
int: M=3;
int: K=8;
int: satTotal;

int: Art=1; int: BD=2; int: Litterature=3; int: Loisirs=4; int: Nature=5; int: Policier=6; int: Politique=7; int: SF=8;

array [1..N] of string: nomPers=["pierre", "jean", "paul", "julien", "ahmed", "marie", "isabelle", "sylvie", "alice", "carole"];

array [1..N] of set of int: preferences=
  [ {2, 8, 4},  {6, 7, 8},  {3, 1},  {4, 5, 2},  {5, 1, 4}, 
    {2, 6, 7},  {3, 7, 4},  {3, 7, 1},  {7, 1, 5},  {4, 5, 1} ];
    
    
array [1..N] of int: affectP=[];

array [1..N] of set of int: livresduGroupe=[];

array [1..N] of int: satP=[];

% le score total est la somme des scores satP[i]
constraint satTotal = sum([satP[i] | i in 1..N]);

% pour chaque personne, le score de sat est le nombre de livres de son groupe qui l'intéresse
constraint forall(i in 1..N) (satP[i]=card(livresduGroupe[affectP[i]] intersect preferences[i]));

% un livre ne peut pas aller dans 2 groupes
constraint forall(i in 1..N, j in 1..M where i<j) (card (livresduGroupe[i] intersect livresduGroupe[j]) =0);

% tous les livres doivent être attriués
constraint array_union(livresduGroupe) = {i | i in 1..K};

%groupes équilibrés en nb de personnes
constraint forall(i in 1..M) (ceil(N/M)-2 <= count(affectP, i) /\ count(affectP, i) <= ceil(N/M)+2);

%groupes équilibrés en nb de livres
constraint forall(i in 1..M) (ceil(K/M)-2 <= card(livresduGroupe[i]) /\ card(livresduGroupe[i]) <= ceil(K/M)+2);
 
maximize satTotal;


