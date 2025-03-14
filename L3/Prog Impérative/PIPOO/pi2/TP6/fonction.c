#include "fonction.h"

struct point{
  double x;
  double y;
};

void affichage(Point* s){
  printf("[%1.2f,%1.2f]\n", s->x, s->y);
}

Point* creer(double a, double b){
  Point *p = malloc(sizeof (struct point));

 (*p).x = a;
 (*p).y = b;

  return p;
}

Point* translation(Point* s, double a, double b){
  return creer(s->x+a, s->y+b);
}

Point* modifier(Point* s, double a, double b){
  (*s).x = a;
  (*s).y = b;

  return s;
}
