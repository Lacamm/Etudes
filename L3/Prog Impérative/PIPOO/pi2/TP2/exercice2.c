#include <stdio.h>
#include <stdlib.h>

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


int syracuse(int n){
  if (n == 1)
    return n;
  else if (syracuse(n-1)%2 == 0){
    int res  =syracuse(n-1)/2;
    printf("%d", res);
    return res;
  }
  else{
    int res = syracuse(n-1)*3+1;
    printf("%d\n", res);
    return res;
  }
}


int fibonacci(int n){
  if (n < 2)
    return n;
  else
    return fibonacci(n-1) + fibonacci(n-2);
}


int coeff(int n, int p){
  if (p == 0 || n==p)
    return 1;
  else
    return coeff(n-1,p-1 )+coeff(n-1,p);
}


int produit(int n){
  int res;
  res = 1;

  while(n!=0){
    printf("%d\n", res);
    res = res * (n%10);
    printf("%d\n", n%10);
    printf("\n");
    n/=10;
  }
      printf("res= %d\n", res);

  return res;
}


int produit_recu(int n){
  if(n<10)
    return n;
  else
    return produit(n/10)*(n%10);
}



int main(){

  factorielle(3);
  printf("\n");

  syracuse(5);
  printf("\n");

  printf("%d\n", fibonacci(8));
  printf("\n");

  printf("%d\n", coeff(7,3));
  printf("\n");

  printf("%d\n", produit(1234));
  printf("\n");

  printf("%d\n", produit_recu(1234));
  printf("\n");





  return EXIT_SUCCESS;
}
