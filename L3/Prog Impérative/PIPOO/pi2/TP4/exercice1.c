#include "fonction.h"

int main(){
  // int* T = tab_init(5,10);
  // int* U = tab_init(5,10);
  // int* V = tab_init(5,10);

  // free(T);
  // free(U);
  // free(V);

  int** DT = tab_double_init(5,10);

  printf("message\n");
  

  for (int i=0; i<5;i++){
    free(DT[i]);
  }
  free(DT);
}
