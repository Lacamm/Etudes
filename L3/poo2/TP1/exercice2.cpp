#include "Point.hpp"

int main() {

  Point *P1 = new Point();
  Point P2(2,3);
  Point *P3 = new Point(2,3);
  (*P1).afficher();
  P2.afficher();
  //delete P1;

  P1->droite(*P3);
  P1->dessiner(*P3);


  return 0;
}
