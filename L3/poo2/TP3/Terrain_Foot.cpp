#include "Terrain_Foot.hpp"

#include <iostream>
#include <string>

using namespace std;

const int largeur_default = 20;
const int longueur_default = 60;
const int rayon_default = 5;


Terrain_Foot::Terrain_Foot(){
    (*this).largeur_surface = largeur_default;
    (*this).longueur_surface = longueur_default;
    (*this).rayon = rayon_default;

    // Terrain::Terrain();
    //(*this).rayon = rayon_default;
}

Terrain_Foot::Terrain_Foot(int longueur, int largeur, int rayon):Terrain(longueur, largeur){
    // (*this).largeur_surface = largeur;
    // (*this).longueur_surface = longueur;
    // (*this).rayon = rayon;

    
    (*this).rayon = rayon;
}

Terrain_Foot::~Terrain_Foot(){}


void Terrain_Foot::build_terrain(char symbole){

    int centre_largeur = (*this).largeur_surface/2;
    int centre_longueur = (*this).longueur_surface/2;

    for(int i=0; i<(*this).largeur_surface; i++){
        string ligne;        
        for(int j=0; j<(*this).longueur_surface; j++){

            if( ((i==centre_largeur+(*this).rayon || i==centre_largeur-(*this).rayon) || (j==centre_longueur+(*this).rayon || j==centre_longueur-(*this).rayon)) &&
                (i>centre_largeur-(*this).rayon-1 && i<centre_largeur+(*this).rayon+1 && j>centre_longueur-(*this).rayon-1 && j<centre_longueur+(*this).rayon+1)){
                ligne+="0";                          
            }

            else if(i==0 || i==(*this).largeur_surface-1 || j==0 || j==(*this).longueur_surface-1 || j==centre_longueur){
                ligne+="*";
            }            
            else{
                ligne += symbole;
            }
        }
        (*this).pelouse_foot += ligne;
        (*this).pelouse_foot += '\n';
    }
    cout << (*this).pelouse_foot;
}

