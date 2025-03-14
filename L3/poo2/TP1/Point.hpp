#ifndef POINT_HPP
#define POINT_HPP
#include <iostream>
#include <list>

class Point {
  private:
    double x;
    double y;
  public:
    Point();
    ~Point();
    Point(double, double);
    void afficher();
    std::list<Point> droite(Point);
    double get_x(); //{ return x; } l'un ou l'autre
    double get_y(); //{ return y; }
    void dessiner(Point);
  };
#endif
