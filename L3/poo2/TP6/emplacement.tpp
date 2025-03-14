template <typename T, typename U>  Emplacement<T,U>::Emplacement() {
    this->cle = 0;
    this->valeur = 0;
    suivant = NULL;
}

template <typename T, typename U>  Emplacement<T,U>::Emplacement(T _cle, U _valeur){
    this->cle = _cle;
    this->valeur = _valeur;
    suivant = NULL;
}

template <typename T, typename U> Emplacement<T,U>::~Emplacement(){}



template <typename T, typename U> bool Emplacement<T,U>::cle_existe(const T cle){
    return this->getValue()==cle;
}

template <typename T, typename U> T Emplacement<T,U>::getKey(){
    return this->valeur;
}


template <typename T, typename U> U Emplacement<T,U>::getValue(){
    return this->cle;
}

