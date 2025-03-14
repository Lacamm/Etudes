#include "rectangle.hpp"

using namespace std;

Rectangle::Rectangle(int longueur, int largeur){
    this->longueur = longueur;
    this->largeur = largeur;
}

Rectangle::Rectangle(const Rectangle &r){
    this->longueur = r.longueur;
    this->largeur = r.largeur;
}

Rectangle::~Rectangle(){}

bool Rectangle::operator < (const Rectangle &r) const {
    return (this->longueur*this->largeur) < (r.longueur*r.largeur);
}

ostream& operator<< (std::ostream&ost, const Rectangle &r){
    ost << r.get_longueur() << "*" << r.get_largeur();
    return ost;
}