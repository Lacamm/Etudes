#include "Terrain.hpp"

#include <iostream>
#include <string>

using namespace std;

const int largeur_default = 20;
const int longueur_default = 60;


Terrain::Terrain(){
    (*this).largeur = largeur_default;
    (*this).longueur = longueur_default;
}

Terrain::Terrain(int longueur, int largeur){
    (*this).largeur = largeur;
    (*this).longueur = longueur;
}

Terrain::~Terrain(){}


void Terrain::build_terrain(char symbole){
    for(int i=0; i<(*this).largeur; i++){
        string ligne;        
        for(int j=0; j<(*this).longueur; j++){
            if(i==0 || i==(*this).largeur-1 || j==0 || j==(*this).longueur-1){
                ligne+="*";
            }
            else{
                ligne += symbole;
            }
        }
        (*this).pelouse += ligne;
        (*this).pelouse += '\n';
    }
    cout << (*this).pelouse;
}