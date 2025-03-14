#include "catalan.h"
#include "pascal.h"

/* Pour compiler, il faut générer les fichiers objets (.o) catalan et pascal 
 * et les lier au main_ifndef.o pour obtenir un exécutable 
 * gcc -std=c99 -Wall -Wextra -pedantic -ggdb -Wno-abi -o catalan.o -c catalan.c
 * gcc -std=c99 -Wall -Wextra -pedantic -ggdb -Wno-abi -o pascal.o -c pascal.c
 * gcc -std=c99 -Wall -Wextra -pedantic -ggdb -Wno-abi -o main_ifndef.o -c main_ifndef.c
 * gcc -std=c99 -Wall -Wextra -pedantic -ggdb -Wno-abi -o executable catalan.o pascal.o main_ifndef.o fonctions.o
 */

int main() {

    printf("%ld\n",catalan(6));
    pascal(6);
    return EXIT_SUCCESS;
}
