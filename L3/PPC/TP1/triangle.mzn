%const locale
int : max = 180;

%déclaration de variables et domaines
var 1..max : a;
var 1..max : b;
var 1..max : c;

%déclaration de contraintes
constraint a+b+c = 180;
constraint 360 mod a = 0;
constraint 360 mod b = 0;
constraint 360 mod c = 0;

%suppr doublons, /\ ET logique
constraint a<=b /\ b<=c;

%lancer solveur
solve satisfy;

%afficher solution
output ["Voici les angles diviseurs de 360:\(show(a)) ,\(show(b)) ,\(show(c))\n"];