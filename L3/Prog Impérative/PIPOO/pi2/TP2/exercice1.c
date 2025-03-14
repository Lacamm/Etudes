#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main() { //int argc, char** argv

  void Premier(int n){
    int pr = 1;
    for (int i = 2; i < n; i++){ //ou while
      if (n%i == 0 && i!=n){
        printf("%s\n", "NON PREMIER" );
        pr = 0;
      }
    }
    if (pr)
      printf("%s\n", "PREMIER" );
  }

  Premier(3);

  bool premier_bool(int n){
    for (int i=2; i<n; i++){
      if(n%i == 0 && i!=n)
        return false;
    }
    return false;
  }

  printf("%d\n",premier_bool(7));


  int fibonacci(int n){
    int a,b,res;
    a = 0;
    b = 1;

    if (n==0)
      res = 0;
    else if(0<n<=2)
      res = 1;
      else{
        for (int i = 3; i < n; i++) {
          res = a + b;
          a = b;
          b = res;
        }
      }

    return res;
  }
  /*
  int fib(int n) {
  int first = 0, second = 1;

  int tmp;
  while (n--) {
    tmp = first+second;
    first = second;
    second = tmp;
  }
  return first;
}
  */

  printf("%d\n",fibonacci(8));

  printf("\n");


  //aurai dû etre en itératif
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

  syracuse(5);






















  return EXIT_SUCCESS;
}
