#include "fonction.h"
#include <time.h>

int main() {

    srand(time(NULL));

    char c1[5] = "truc";
    char c2[6] = "kayak";

    char alphabet[27] = "abcdefghijklmnopqrstuvwxyz";

    printf("c1 palindrome? %d\n",palindrome(c1)); // 0
    printf("c2 palindrome? %d\n",palindrome(c2)); // 1
    printf("\n");

    char* res = concatene(c2,c1);
    printf("concatenation : %s\n",res);
    printf("\n");
    free(res);

    char car = alphabet[rand() % 27];
    int pos = rand() % strlen(c2);

    char* copy[strlen(c2)];
    strcpy(copy,c2);
    printf("ajout de %c dans %s à la position %d : %s\n", car, c2, pos, modif(copy, car, pos));


    return EXIT_SUCCESS;
}
