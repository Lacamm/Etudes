#include <stdio.h>
#include <stdlib.h>

int main(){
  int trie [5] = { 1, 2, 2, 4, 8 };
  int non_trie [5] = { 1, 4, 3, 5, 8 };
  int sans_doublons [5] = { 2, 3, 4, 6, 8 };
  int avec_doublons [5] = { 2, 3, 3, 6, 8 };

 /******** trie  ********/
 int tri = 1;
  for (int i=1; i<5; i++){
    if (trie[i-1]>trie[i]){
      printf("La liste n'est pas triée dans l'ordre croissant\n");
      tri = 0;
      break;
    }
  }
  if (tri == 1)
  printf("La liste est triée dans l'ordre croissant\n");
  printf("\n");

  /******** non_trie  ********/
  int tri2 = 1;
  for (int i=1; i<5; i++){
    if (non_trie[i-1]>non_trie[i]){
      printf("La liste n'est pas triée dans l'ordre croissant\n");
      tri2 = 0;
      break;
    }
  }
  if (tri2 == 1)
  printf("La liste est triée dans l'ordre croissant\n");
  printf("\n");

  /******** sans_doublons  ********/
  int doubl = 0;
  for (int i=0; i<5; i++){
    for (int j=+1; j<5; j++){
      if (sans_doublons[i] == sans_doublons[j] && i!=j){
        printf("La liste comporte des doublons\n");
        doubl = 1;
        break;
      }
    }
    if(doubl == 1)
      break;
  }
  if(doubl == 0)
    printf("La liste ne comporte pas de doublons\n");
  printf("\n");

  /******** avec_doublons  ********/
  int doubl1 = 0;
  for (int i=0; i<5; i++){
    for (int j=i+1; j<5; j++){
      if (avec_doublons[i] == avec_doublons[j] && i!=j){
        printf("La liste comporte des doublons\n");
        doubl1 = 1;
        break;
      }
    }
    if(doubl1 == 1)
      break;
  }
  if(doubl1 == 0)
    printf("La liste ne comporte pas de doublons\n");
  printf("\n");
}
