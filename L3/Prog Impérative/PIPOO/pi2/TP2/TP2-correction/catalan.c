#include "catalan.h"

long int catalan(int n) {
    return factorielle(2*n)/((factorielle(n+1)*factorielle(n)));
    //return coefficient(2*n,n)/(n+1);
}
