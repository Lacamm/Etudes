#include "Point.hpp"
using namespace std;

Point::Point() {
  cout << "Constructeur par defaut." << endl;
  (*this).x = 0;
  (*this).y = 0;
}

Point::Point(double x, double y) {
  (*this).x = x;
  (*this).y = y;
}

Point::~Point() {
  cout << "Destructeur" << endl;
}

double Point::get_x() { return (*this).x; }
double Point::get_y() { return (*this).y; }

void Point::afficher() {
  cout << "[" << (*this).x << "," << (*this).y << "]" << endl;
}

list<Point> Point::droite(Point p){
  double e = p.x - (*this).x;
  double dx = e * 2;
  double dy = ((*this).y - p.y) * 2;
  list<Point> points;

  while ((*this).x <= p.x){
    points.push_back(Point((*this).x, p.y));
    (*this).x = (*this).x+1;
    e = e -dy;

    if(e<=0){
      (*this).y = (*this).y +1;
      e = e + dx;
    }
  }
  return points;
}

void Point::dessiner(Point p){
  int taille_carre = 25;
  list<Point> liste = this->droite(p);
  list<Point>::iterator it;

  for (int i=0; i< taille_carre; i++){
    for (int y=0; y<taille_carre; y++){
      for (it = liste.begin(); it != liste.end(); it++) {
        if(i==0 || i==taille_carre || y==0) {cout << "#";}
        else if (y==taille_carre) {cout << "#" << endl;}
        else if (i==p.x && y==p.y) {cout << "o";}
        else if (i==(*this).x && y==(*this).y) {cout << "o";}
        else if((*it).x==i && (*it).y==y){cout << "x";}
        else {cout << " ";}
      }
    }
  }
}
