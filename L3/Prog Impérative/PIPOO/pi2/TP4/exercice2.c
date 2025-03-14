#include "fonction.h"

int main(){
  int n = 11;

  int* tab = tab_init(n,3);

  for(int i=0;i<n;i++){
    printf("%d\n",tab[i]);
  }


  printf("elem majoritaire: %d\n",estMajoritaire(tab, n));

  printf("Boyer_Moore: %d\n",Boyer_Moore(tab, n));
}
