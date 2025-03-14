#ifndef TERRAIN_HPP
#define TERRAIN_HPP

#include <iostream>
#include <string>

class Terrain {
    protected:
        int longueur;
        int largeur;
        std::string pelouse;

    public:
        Terrain();
        Terrain(int, int);
        virtual ~Terrain();
        virtual void build_terrain(char);
};

#endif