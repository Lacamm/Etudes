#include <stdlib.h>
#include <stdio.h>
#include <assert.h> 

long int factorielle(int);
void syracuse(int);
int fibonacci(int);
long int coefficient_binomial(int, int);
long int coefficient_binomial_recursif(int, int);
long int produit(int);
long int produit_terminal(int);

int main() {
    printf("%ld\n", factorielle(7));
    syracuse(10);
    printf("%ld\n",coefficient_binomial(20,8));
    printf("%ld\n",coefficient_binomial_recursif(20,8));
    printf("%ld\n", produit(1234));
    printf("%ld\n", produit_terminal(10234));
    int terme = 8;
    printf("%d neme terme de Fibonacci : %d\n", terme, fibonacci(terme));
    return EXIT_SUCCESS;
}

/* Pré-condition : on suppose n >= 0*/
long int factorielle(int n) {
    /* Condition d'arrêt */
    if(n<=1) 
        return 1;
    /* Appel récursif sur le paramètre n-1 */
    return n*factorielle(n-1);
}

/* Pré-condition : on suppose n > 0 */
void syracuse(int n) {
    /* Condition d'arrêt : affichage d'un retour à la ligne */
    if(n==1)
        printf("%d\n", n);
    else {
        /* Affichage du paramètre */
        printf("%d\t", n);
        /* Appel récursif en fonction de la parité de n */
        if (n%2==0) 
            syracuse(n/2);
        else 
            syracuse(3*n+1);
    }
}

/* Pré-condition : on suppose n >= 0*/
int fibonacci(int n) {
    if(n == 0)
        return 0;
    if(n <= 2)
        return 1;
    else
        return fibonacci(n-1)+fibonacci(n-2);
}

/* Pré-condition : on suppose n > 0, m >= 0 et n >= m */
long int coefficient_binomial_recursif(int n, int m) {
    if(m == 0 || m == n)
        return 1;
    else
        return coefficient_binomial(n-1,m-1) + coefficient_binomial(n-1,m);
}

/* Pré-condition : on suppose n > 0, m >= 0 et n >= m */
long int coefficient_binomial(int n, int m) {
    return factorielle(n) / (factorielle(m) * factorielle(n-m));
}

long int produit(int n) {
    /* Condition d'arrêt : si n contient un 0, on retourne 0 */
    if(n%10 == 0)
        return 0;
    /* Condition d'arrêt : si n contient un seul chiffre m, on retourne m */
    if((int)n/10 == 0)
        return n;
    /* Appel récursif : division par 10 pour décalage à gauche */
    return (n%10)*produit((int)n/10);
}

/* Version récursive terminale : l'appel récursif est la dernière opération de la 
 * fonction. Les appels récursifs précédents ne sont donc pas mis "en attente"
 * Remarque -- une fonction déclarée static ne peut être utilisée que dans le fichier 
 * qui la contient. 
 */
static long int produit_rec(int n, int resultat) {
    /* Pour obtenir un algorithle récursif terminal, le résultat 
     * est propagé dans les paramètres au lieu d'être calculé au sein 
     * des appels récursifs
     */
    if(n%10==0)
        return 0;
    /* Condition d'arrêt : on retourne le résultat calculé jusque là multiplié par n */
    if((int)n/10==0)
        return resultat*n;
    return produit_rec((int)n/10,resultat*(n%10));
}

long int produit_terminal(int n) {
    return produit_rec(n,1);
}
