#ifndef TERRAIN_FOOT_HPP
#define TERRAIN_FOOT_HPP

#include "Terrain.hpp"

#include <iostream>
#include <string>

class Terrain_Foot : public Terrain{

    private:
        int largeur_surface;
        int longueur_surface;
        int rayon;
        std::string pelouse_foot;

    public:
        Terrain_Foot();
        Terrain_Foot(int, int, int);
        ~Terrain_Foot();
        void build_terrain(char);
};

#endif