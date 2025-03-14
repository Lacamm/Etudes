#ifndef KMEANS_HPP
#define KMEANS_HPP
#include <iostream>
#include <map>
#include <vector>
#include "Point.hpp"

using namespace std;

class Kmeans {
  private:
    vector<Point> v; //liste de points
    map<int, int> liste; //liste indice association point/centre
    int k; //nombre de cluster
    vector<Point> tab; //tableau des centroïdes
  public:
    Kmeans();
    Kmeans(int, int);
    ~Kmeans();
    void initialiser();
    void calculer(int);
    void csv();
  };

#endif
