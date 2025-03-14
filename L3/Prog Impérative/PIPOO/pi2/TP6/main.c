#include "fonction.h"

int main(){

  Point *p = creer(2,3);
  affichage(p);

  Point *p2 = translation(p,7,15);
  affichage(p2);
  free(p2);

  modifier(p, 5,6);
  affichage(p);
  free(p);


  int taille = 2;
  Chemin *c = generation(taille,1,9);
  affichage_chemin(c);
  liberer(c);

}
