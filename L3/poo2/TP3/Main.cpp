#include "Terrain.hpp"
#include "Terrain_Foot.hpp"
#include "Terrain_Rugby.hpp"

int main(){
    using namespace std;

    // Terrain t1;
    // Terrain t2(5, 10);

    // t1.build_terrain('|');
    // t2.build_terrain('/');

    // Terrain_Foot tf1;
    // tf1.build_terrain('|');

    Terrain* tr1 = new Terrain_Rugby();
    tr1->build_terrain('|');

    return 0;
}