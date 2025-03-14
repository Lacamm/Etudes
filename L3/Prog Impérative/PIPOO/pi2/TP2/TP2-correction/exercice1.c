#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

/* Remarque : pas de surcharge de fonction en C */
void premier(int);
bool premier_booleen(int);
int fibonacci(int);
void syracuse(int);

int main() {

    int p=0;
    premier(15);
    
    /* Exemple d'utilisation de la fonction scanf */
    printf("Saisir un entier : ");
    /* Attention : la chaîne de caractères du scanf ne doit contenir 
     * que des options de formatage
     */
    scanf("%d", &p);
    printf("Vous avez saisi : %d\n", p);

    if(premier_booleen(p))
        printf("%d est premier\n",p);
    else
        printf("%d n'est pas premier\n",p);

    syracuse(10);

    int terme = 8;
    printf("%d neme terme de Fibonacci : %d\n", terme, fibonacci(terme));

}

/* Pour que cette correction fonctionne, la variable i *doit* être déclarée 
 * à l'extérieur de la boucle : sans ça, elle n'est connue que dans la 
 * portée du for (le bloc défini par les accolades)
 */
void premier(int n) {
    int i;
    for(i = 2; i <n; ++i) {
        if(n%i == 0) {
            printf("%d n'est pas premier\n",n);
            /* Permet d'interrompre l'exécution de la boucle for */
            break;
        }
    }
    if(i==n)
        printf("%d est premier\n", n);
}

/* Pré-condition : n est un entier >= 1 
 * L'utilisation d'une boucle for est également possible 
 * (voir code commenté en fin de fonction) 
 */
bool premier_booleen(int n) {
    if(n <= 2)
        return true;
    bool est_premier = true;
    int diviseur = 2;
    while(diviseur < n && est_premier) {
        if(n % diviseur == 0)
            est_premier = false;
        else
            diviseur++;
    }
    return est_premier;
    /*for(int i = 2; i < n; ++i) {
        if(n % i == 0)
            return false;
    }
    return true;*/
}

/* Le nème terme de la suite de Fibonacci est égal à la somme 
 * des deux précédents ; l'utilisation de 3 variables permet 
 * de facilement réaliser ce calcul. Ici est présentée une version 
 * avec seulement deux variables. A l'itération i, si on a :
 * resultat = 8 et precedent = 5
 * On obtient à l'itération i+1
 * resultat += 5 -> 13 et precedent = 13 - 5 -> 8
 * On peut donc montrer comme invariant de boucle : 
 * "la variable resultat contient le ième terme de la suite de Fibonacci"
 * Pré-condition : n >= 0
 */
int fibonacci(int n) {
    if(n==0)
        return 0;
    if(n<=2)
        return 1;
    int resultat = 2;
    int precedent = 1;
    for(int i = 3; i <= n; ++i) {
        resultat += precedent;
        precedent = resultat - precedent;
    }
    return resultat;
}

/* Affichage de la suite de Syracuse */
void syracuse(int n) {
    /* \t affiche une tabulation
     * \n affiche un retour à la ligne
     */
    printf("%d\t",n);
    while(n != 1) {
        printf("%d\t", n);
        if(n%2==0)
            n=n/2;
        else
            n=3*n+1;
    }
    printf("%d\n",n);
}
