#include "fonction.h"

int main() {

  char* c1 = "TEST";
  char* cle = "ABCD";
  char** table = table_vigenere();
  // for (int i=0;i<26;i++){
  //   printf("%s\n",table[i]);
  // }

  char* code = chiffrer(c1,cle,table);
  printf("%s chiffré donne : %s\n",c1,code);


  char* res = dechiffrer(code,cle,table);
  printf("%s déchiffré donne : %s\n",code, res);

  // free(code);
  // free(res);
  // for (int i=0;i<26;i++){
  //   free(table[i]);
  // }
  // free(table);

  return EXIT_SUCCESS;
}
