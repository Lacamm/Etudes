int: NPERS = 10;
int: NTABLES=3;
int: CAPACITE=4;
int: NMETS=14;

array [1..NPERS] of string: 
NOMPERS=["pierre", "jean", "paul", "julien", "ahmed", "marie", "isabelle", "sylvie", "alice", "carole"];

array [1..NMETS] of string: 
METS=["oeufs", "jambon", "asperges", "pate", "sardines", "salade", "poisson", "gratin", "roti", "poulet","yaourt","ananas","tarte","banane"];

set of int: ENTREES = {1,2,3,4,5,6};
set of int: PLATS = {7,8,9,10};
set of int: DESSERTS = {11,12,13,14};

array [1..NPERS] of set of 1..NMETS: 
APPORTE = [
{1,13}, % pierre: oeufs, tartes
{2,14}, % jean : jambon, banane
{3,11}, % paul : asperge, yaourt
{4,12}, % julien : paté, ananas
{5,12}, % ahmed : sardines, ananas
{6,7}, % marie : salade, poisson
{3,8}, % isabelle : asperge, gratin
{9,13}, % sylvie : roti, tarte
{2,10}, % alice : jambon, poulet
{10,11} % carole : poulet, yaourt
];

array [1..NPERS] of set of int: 
DETESTE= [
{9,10}, % pierre : roti, poulet
{7,10}, % jean : poisson, poulet
{8,7}, % paul : gratin, poisson
{7,9,10}, % julien : poisson, roti, poulet
{8,9}, % ahmed : gratin, roti
{12,14}, % marie : ananas, banane
{11,13}, % isabelle : yaourt, tarte
{2,4,5}, % sylvie : jambon, pate, sardines
{13,14}, % alice : tarte, banane
{2,4,5} % carole : jambon, pate, sardines
];


array[1..NPERS] of var 1..NTABLES: placrPers;

array[1..NTABLES] of var set of 1..NMETS: metsTable;

array[1..NPERS, 1..NTABLES] of var set of 1..NMETS: apporte =  [|{1,13},{2,14},{3,11}
                                                                |{4,12},{5,12},{6,7}
                                                                |{3,8},{9,13},{2,10}
constraint forall(i in 1..NPERS, jin 1..NTABLES)(
  if placerPer[i]=j then 
    apporte[i,j] = apporte[i]
  else
    apporte[i,j] = {}
  endif
);

constraint forall(i in 1..NTABLES)(metsTables[j] = array_union(i in 1..NPERS)(apporte[i,j]) /\card(metsTables[j])
intersect ENTREES) != 0);

constraint forall(i in 1..NPERS)(card(ENTREES intersect(metsTable[placerPer[i]] diff DETESTE[i])) != 0);

















