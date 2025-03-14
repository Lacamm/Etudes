#include <assert.h>
#include "fonctions.h"

/* Pré-condition : on suppose n >= 0*/
long int factorielle(int n) {
    if(n<=1) 
        return 1;
    return n*factorielle(n-1);
}

/* Pré-condition : on suppose n > 0, m >= 0 et n >= m */
long int coefficient(int n, int m) {
    return factorielle(n) / (factorielle(m) * factorielle(n-m));
}

