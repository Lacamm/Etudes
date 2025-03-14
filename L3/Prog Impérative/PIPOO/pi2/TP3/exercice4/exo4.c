#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool est_triee(int tab, int taille){
  for (int i=1; i<taille; i++){
     if (tab[i-1]>tab[i]){
       return false;
     }
   }
  return true;
}

bool doublon(int tab, int taille){
  for (int i=0; i<taille; i++){
    for (int j=+1; j<taille; j++){
      if (tab[i] == tab[j] && i!=j){
        return false;
      }
    }
  }
  return true;
}

int main(){
  int trie [5] = { 1, 2, 2, 4, 8 };
  int non_trie [5] = { 1, 4, 3, 5, 8 };
  int sans_doublons [5] = { 2, 3, 4, 6, 8 };
  int avec_doublons [5] = { 2, 3, 3, 6, 8 };

  est_triee(trie,5);
  printf("\n");

  est_triee(non_trie,5);
  printf("\n");

  doublon(sans_doublons,5);
  printf("\n");

  doublon(avec_doublons,5);
  printf("\n");

}
