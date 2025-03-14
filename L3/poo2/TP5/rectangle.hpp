#ifndef RECTANGLE_HPP
#define RECTANGLE_HPP

#include <iostream>

class Rectangle {

    private:
        int longueur;
        int largeur;
    
    public:
        Rectangle(int longueur, int largeur);
        Rectangle(const Rectangle &r);
        ~Rectangle();

        int get_longueur() const {return longueur;}
        int get_largeur() const {return largeur;}

        bool operator < (const Rectangle &r) const;
};

std::ostream& operator<< (std::ostream&ost, const Rectangle &r);

#endif