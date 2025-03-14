#include "fonction.h"

bool palindrome(char* chaine){
  for (int i=0; i<(int)strlen(chaine);i++){
    if (chaine[i] != chaine[strlen(chaine)-(i+1)]){
      return false;
    }
  }
  return true;
}


char* concatene(char* c1, char* c2){
  char* res = (char*) malloc( (strlen(c1)+strlen(c2)+1) * sizeof(char));
  strcpy(res,c1);
  return strcat(res,c2);
}


char* modif(char* c1, char car, int pos){
  c1[pos] = car;
  return c1;
}

char* cesar(char* c1, int cle){
  char* res = (char*) malloc( (strlen(c1)+1) * sizeof(char));

  for (int i=0; i<(int)strlen(c1);i++){
    res[i] = ((c1[i]-65)+cle)%26 + 65;
  }
  return res;
}


char** table_vigenere(){
  char** res = (char**) malloc(26 * sizeof(char*));

  for (int i=0;i<26;i++){
    res[i] = (char*) malloc(26 * sizeof(char));
  }

  for (int i=0;i<26;i++){
    for (int j=0;j<26;j++){
      res[i][j] = ((i)+j)%26 + 65;
    }
  }
  return res;
}


char* chiffrer(char* msg, char* cle, char** table){
  char* res = (char*) malloc( (strlen(msg)+1) * sizeof(char));

  for (int i=0;i<(int)strlen(msg);i++){
    res[i] = table[cle[i]-65][msg[i]-65];
  }
  return res;
}


char* dechiffrer(char* msg, char* cle, char** table){ //a finir
  char* res = (char*) malloc( (strlen(msg)+1) * sizeof(char));

  for (int i=0;i<(int)strlen(msg);i++){

    while (int a<25 || table[cle[i]-65] == [msg[i]-65]{
      i++;
    }
    table[cle[i]-65]


    res[i] = [msg[i]-65];
    //res[i] = (msg[i]+cle[i])%26 + 65;
  }
  return res;
}
