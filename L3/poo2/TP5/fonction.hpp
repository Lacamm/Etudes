#ifndef FONCTION_HPP
#define FONCTION_HPP

#include <iostream>
#include <vector>
#include <map>

using namespace std;

template <typename T> T maximum(const T &a, const T &b);

template <typename T> T somme(const vector<T> &v);

template <typename T> vector<T> tri_panier( const vector<T> &v);


#include "fonction.tpp"

#endif