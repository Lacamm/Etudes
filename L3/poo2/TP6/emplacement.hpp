#ifndef EMPLACEMENT_HPP
#define EMPLACEMENT_HPP

#include <iostream>

using namespace std;

template <typename T, typename U> class Emplacement {
    private:
        T cle;
        U valeur;
        Emplacement<T,U> * suivant;
    
    public:
        Emplacement();
        Emplacement(T _cle, U _valeur);
        //Emplacement(const T &e);
        ~Emplacement();

        bool cle_existe(const T cle);
        T getKey();
        U getValue();
};

#include "emplacement.tpp"

#endif