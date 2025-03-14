#ifndef TERRAIN_RUGBY_HPP
#define TERRAIN_RUGBY_HPP

#include "Terrain.hpp"

#include <iostream>
#include <string>

class Terrain_Rugby: public Terrain {
    private:
        int longueur;
        int largeur;
        std::string pelouse;

    public:
        Terrain_Rugby();
        Terrain_Rugby(int, int);
        ~Terrain_Rugby();
};

#endif