#ifndef TABLE_HACHAGE_HPP
#define TABLE_HACHAGE_HPP

#include <iostream>
#include <list>

#include "emplacement.hpp"

using namespace std;

template <typename T, typename U > class table_hachage {
    private:
        size_t taille;
        list<Emplacement<T,U> * > table;

    public:
        table_hachage(size_t taille);
        ~table_hachage();

        bool acces(const T &cle, U& retour);
        void inserer(const T &cle, const U &value);
        void supprimer(const T &cle);
};


#include "table_hachage.tpp"

#endif