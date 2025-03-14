#ifndef FONCTION_H
#define FONCTION_H

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//#include <stdbool.h>

int* tab_init(int n, int m);
int** tab_double_init(int n, int m);

int estMajoritaire(int* tab, int n);
int Boyer_Moore(int* tab, int n);

long int factorielle(int n);
int nbDeplacements(int n, int m);

#endif
