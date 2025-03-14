#ifndef FONCTION_H
#define FONCTION_H

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool palindrome(char* chaine);

char* concatene(char* c1, char* c2);

char* modif(char* c1, char car, int pos);

char* cesar(char* c1, int cle);

char** table_vigenere();

char* chiffrer(char* msg, char* cle, char** table);

char* dechiffrer(char* msg, char* cle, char** table);

#endif
