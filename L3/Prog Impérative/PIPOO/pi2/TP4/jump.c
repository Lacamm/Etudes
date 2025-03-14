#include <stdlib.h>
#include <stdio.h>

int main() {

    int* tab = (int*)malloc( 10*sizeof(int) );
    printf("%d\n", tab[3]);

    free(tab);
    return EXIT_SUCCESS;
}
