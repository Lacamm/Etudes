#ifndef FONCTION_H
#define FONCTION_H

#include <stdio.h>
#include <stdlib.h>

typedef struct point Point;
typedef struct chemin Chemin;

void affichage(Point*);
Point* creer(double x, double y);
Point* translation(Point*, double a, double b);
Point* modifier(Point*, double a, double b);

Chemin* generation(int n, int min, int max);
void liberer(Chemin* c);
void affichage_chemin(Chemin* c);

#endif
