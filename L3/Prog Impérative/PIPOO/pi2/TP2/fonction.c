#include <fonction.h>

int factorielle(int n){
  int res = 0;
  if (n == 0 || n == 1){
    return n;
  }
  else{
    res = factorielle(n-1)*n;
  }
  printf("%d\n", res);
  return res;
}

int coeff(int n, int p){
  if (p == 0 || n==p)
    return 1;
  else
    return coeff(n-1,p-1 )+coeff(n-1,p);
}
