#include "fonction.hpp"
#include "rectangle.hpp"
#include "point.hpp"

#include <stdlib.h>
#include <time.h>

int main() {

    srand (time(NULL));


    cout << maximum(3,5) << endl;
    cout << maximum(6.2, 9.3) << endl;

    Rectangle r1 = Rectangle(2,8);
    Rectangle r2 = Rectangle(3,7);

    cout << maximum(r1,r2) << endl;

    vector<int> v1;
    cout << somme(v1) << endl;

    vector<float> v2;
    for (int i=0; i<5; i++){
        float r = static_cast <float> (rand()) / (static_cast <float> (RAND_MAX/10));
        v2.push_back(r);
    }
    cout << somme(v2) << endl;



    vector<int> v3;
    for (int i=0; i<5; i++){
        int r = static_cast <int> (rand()) / (static_cast <int> (RAND_MAX/10));
        v3.push_back(r);
    }
    cout << somme(v3) << endl;

    vector<Point> v4;
    for (int i=0; i<5; i++){
        Point p = Point(rand() % 100,rand() % 100);
        v4.push_back(p);
    }
    cout << somme(v4) << endl;


    vector<int> v5;
    for (int i=0; i<5; i++){
        int r = rand() % 3;
        v5.push_back(r);
    }
    vector<int> v5t = tri_panier(v5);

    vector<float> v6;
    for (int i=0; i<5; i++){
        float r = static_cast <float> (rand()) / (static_cast <float> (RAND_MAX/3));
        v6.push_back(r);
    }
    vector<float> v6t = tri_panier(v6);

    for (int i=0; i<v5t.size();i++){cout << v5t[i] << endl;}
    for (int i=0; i<v6t.size();i++){cout << v6t[i] << endl;}

    return 0;
}

