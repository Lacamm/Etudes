#include "emplacement.hpp"
#include "table_hachage.hpp"


int main(){

    Emplacement<int,float> e1 = Emplacement<int,float>(1,10.25);
    Emplacement<int,float> e2 = Emplacement<int,float>(5, 8.75);
    Emplacement<int,float> e3 = Emplacement<int,float>();

    table_hachage<int,float> t1 = table_hachage<int, float>(5);

    float val = 0.0;
    t1.acces(1,val);
    cout << val << endl;
    t1.acces(48, val);
    cout << val <<endl;

    // t1.inserer(e2);
    // t1.inserer(e3);

    // t1.supprimer(e2);
    // t1.supprimer(e3);


    return 0;
}