#include "Kmeans.hpp"
#include <stdlib.h>
#include <cmath>
#include <fstream>

using namespace std;

Kmeans::Kmeans() {
  cout << "Constructeur par defaut." << endl;
  (*this).k = 0;
}

Kmeans::Kmeans(int n, int k) {
  (*this).k = k;
  for(int i=0;i<n;i++){
    Point p(rand()%30, rand()%30);
    (*this).v.push_back(p);
  }
}

Kmeans::~Kmeans() {
  cout << "Destructeur" << endl;
}

void Kmeans::initialiser() {
  vector<int> listeIndice;
  int indice = rand()%(*this).k;

  for (int i=0; i<(*this).k; i++){
    bool dejaPresent = false;

    while(dejaPresent){
      int indice = rand()%(*this).k;
      for (int j=0;j<i;j++){
        if(indice == listeIndice.at(j)){
          dejaPresent = true;
          break;
        }
      }
    }
    if(!dejaPresent){
      listeIndice.push_back(indice);
      (*this).tab.push_back((*this).v.at(indice));
    }
  }
}

void Kmeans::calculer(int duree) {
  for(int a=0; a<duree; a++){
    for(int i=0;i<(int)(*this).v.size();i++){
      double taille = 100;
      int centre = -1;
      int point = -1;
      for(int j=0;j<(int)(*this).tab.size();j++){
        double res = abs(sqrt(pow(((*this).v.at(i).get_x()-(*this).tab.at(j).get_x()),2)+pow(((*this).v.at(i).get_y()-(*this).tab.at(j).get_y()),2)));
        if (res < taille){
          taille = res;
          centre = j;
        }
      }
     (*this).liste[i] = centre;
    }

    vector<int>listeCluster;
    for(int i=0;i<(int)(*this).liste.size();i++) {
      listeCluster.push_back(0);
      int centre = (*this).liste[i];
      int point = i;
      (*this).tab.at(centre).set_x((*this).v.at(point).get_x()+(*this).tab.at(centre).get_x());
      (*this).tab.at(centre).set_y((*this).v.at(point).get_y()+(*this).tab.at(centre).get_y());
      listeCluster[centre]++;
    }
    int taille = (int) (*this).tab.size();
    for(int j=0; j<taille; j++){
      (*this).tab.at(j).set_x((double)(*this).tab.at(j).get_x()/listeCluster[j]);
      (*this).tab.at(j).set_y((double)(*this).tab.at(j).get_y()/listeCluster[j]);
    }
  }
}

void Kmeans::csv(){
  // ifstream myfile("donnees.csv");
  // int x; int y;
  // while(myfile >> x >> y) {
  //   cout << x << " " << y << endl;
  // }
  // myfile.close();


  std::ofstream myfile;
    myfile.open ("output.csv");
    myfile << "x,y,c" << std::endl;

    for(int=0; i<this->v.size(); i++){
      myfile << this->v.get_x() << "," << this->v.get_y() << "," << //this->liste[i]  //récupérer la valeur associée à la clé i
    }
    myfile.close();



}
