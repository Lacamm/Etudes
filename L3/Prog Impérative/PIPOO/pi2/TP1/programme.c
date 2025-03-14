/* Inclusion des librairies standard */
#include <stdlib.h> // EXIT_SUCCESS
#include <stdio.h> // Fonctions usuelles (printf, ...)
#include <math.h> // Fonctions Mathématiques

int main(int argc, char** argv) {

    printf("Affichage d'un entier avec retour à la ligne : %d\n", 5);

    printf("entier : %i\n", 10);

    puts("Hello world\n");

    printf("char : %c \n", 's');

    /* EXIT_SUCCESS est une constante définie à la valeur 0
     * #define	EXIT_SUCCESS	0
     */

     /* Entier Parfait */
     int a = 6;
     int b = 0;

     for(int i=1; i<a; i++){
       if(a%i == 0){
         b = b+i;
       }
     }
     if(a == b){
       printf("%i%s", a," est un entier parfait\n");
     }

     // printf("a = %i\n",a);
     // printf("b = %i\n",b);

     /* Nombre de Münchhausen */

     int n = 3435;
     int m = n;
     int r = 0;


     while (m!=0){
       int mod = m%10;
       r = r + pow(mod,mod);
       m/=10;
     }
     if(n == r){
       printf("%i%s", n," est un nombre de Münchhausen\n");
     }



    return EXIT_SUCCESS;

}
