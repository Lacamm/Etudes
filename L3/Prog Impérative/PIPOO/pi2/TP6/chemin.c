#include "fonction.h"
#include <time.h>

struct chemin{
  Point** tab;
  int sommet;
};

Chemin* generation(int n, int min, int max){
  srand(time(NULL));

  Chemin *c = malloc(sizeof(struct chemin));
  c->tab = malloc(n*sizeof(Point*));

  for (int i=0; i<n; i++){
    printf("i=%d\n",i);

    int z = (double) (rand() % min + max);
    int e = (double) (rand() % min + max);
    c->tab[i]=creer(z,e);
  }
  c->sommet = n;

  return c;
}

void affichage_chemin(Chemin* c){
  printf("lg=%d\n",c->sommet);
  for (int i=0; i<c->sommet;i++){
    affichage(c->tab[i]);
  }
  printf("%d",c->sommet);
}

void liberer(Chemin* c){
  for (int i=0; i<c->sommet;i++){
    free(c->tab[i]);
  }
  free(c->tab);
  free(c);
}
