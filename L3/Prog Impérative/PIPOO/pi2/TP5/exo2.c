#include "fonction.h"

int main() {

  char* c1 = "ABC";
  int cle = 1;

  char* copy[strlen(c1)];
  strcpy(copy,c1);
  char* res = cesar(copy,cle);

  printf("code césar appliqué à %s avec clé de %d donne : %s\n", c1, cle, res);
  free(res);

  return EXIT_SUCCESS;
}
