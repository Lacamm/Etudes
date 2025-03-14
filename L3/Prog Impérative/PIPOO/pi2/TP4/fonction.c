#include "fonction.h"

int* tab_init(int n, int m){
  int* tab = (int*) malloc(n*sizeof(int));
  srand (time(NULL));

  for (int i=0;i<n;i++){
    tab[i] = rand()%m;
  }
  return tab;
}

int** tab_double_init(int n, int m){
  int** double_tab = (int**) malloc(n*sizeof(int*));

  for (int i=0;i<n;i++){
    double_tab[i] = (int*) malloc(n*sizeof(int));
  }
  srand (time(NULL));

  for (int i=0;i<n;i++){
    for (int j=0;j<n;j++){
      double_tab[i][j] = rand()%m;
    }
  }

  return double_tab;
}

int estMajoritaire(int* tab, int n){ // O(n log(n)) --> diviser pour régner

  for(int i=0;i<n;i++){
    int cpt = 0;

    for(int j=0;j<n;j++){
      if (tab[j] == tab[i])
        cpt++;
    }
    if (cpt >= (n/2)+1)
      return tab[i];
  }
  return -1;
}

int Boyer_Moore(int* tab, int n){

  int cpt = 0;
  int candidat;

  printf("cpt= %d\n",cpt);
  printf("candidat= %d\n",candidat);

  for (int i=0;i<n;i++){
    if(cpt == 0){
      candidat = tab[i];
      cpt++;
    }
    else if(candidat == tab[i])
      cpt++;
    else if (candidat != tab[i])
      cpt--;

    printf("cpt= %d\n",cpt);
    printf("candidat= %d\n",candidat);
  }


  if (cpt >= (n/2)+1) //a refaire
    return 1;
  else
    return -1;
} // trouve si il y a un elem majoritaire

long int factorielle(int n) {
    if(n<=1)
        return 1;
    return n*factorielle(n-1);
}

int nbDeplacements(int n, int m){
  return factorielle(n+m)/(factorielle(n)*factorielle(m));
}
