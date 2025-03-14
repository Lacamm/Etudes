#include "Terrain_Rugby.hpp"
#include "Terrain.hpp"

#include <iostream>
#include <string>

using namespace std;

const int largeur_default = 20;
const int longueur_default = 60;


Terrain_Rugby::Terrain_Rugby():Terrain(){
    // (*this).largeur = largeur_default;
    // (*this).longueur = longueur_default;
}

Terrain_Rugby::Terrain_Rugby(int longueur, int largeur):Terrain(longueur, largeur){
    // (*this).largeur = largeur;
    // (*this).longueur = longueur;
}

Terrain_Rugby::~Terrain_Rugby(){}
