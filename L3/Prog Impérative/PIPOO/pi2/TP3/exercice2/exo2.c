#include <stdio.h>
#include <stdlib.h>

void carre(int a){
  a = a*a;
  printf("a = %d\n", a);
}

void echange(int a, int b){
  int c = a;
  a = b;
  b = c;
  //printf("a = %d\n", a);
  //printf("b = %d\n", b);
}

void adresse(int *x, int *y, int *z){
  int a = *x;
  int b = *y;
  int c = *z;

  if (a>b){
    int c = a;
    a = b;
    b = c;
  }
  else if (a>c){
    int d = a;
    a = c;
    c = d;
  }
  else if (b>c){
    int d = b;
    b = c;
    c = b;
  }

  printf("a = %d\n", a);
  printf("\n");
  printf("b = %d\n", b);
  printf("\n");
  printf("c = %d\n", c);
  printf("\n");
}

int main(){

  int n = 6;
  carre(n);
  printf("\n");

  int m = 45;
  echange(n,m);
  printf("\n");

  int x,y,z;
  x = 48;
  y = 12;
  z = 26;
  adresse(&x,&y,&z);
  printf("\n");

}
