template <typename T, typename U>
    table_hachage<T,U>::table_hachage(size_t taille){
        this->taille = taille;
    }

template <typename T, typename U>
    table_hachage<T,U>::~table_hachage(){}


template <typename T, typename U>
    bool table_hachage<T,U>::acces(const T &cle, U& retour){

        for (size_t i=0; i<this->taille; i++){
            if (this->table[i].cle_existe(cle)){
                retour = this->table[i].getValue();
                return true;
            }
        }
        return false;
    }

template <typename T, typename U>
    void table_hachage<T,U>::inserer(const T &cle, const U &value){

        Emplacement<T,U> e = Emplacement<T,U>(cle,value);
        this->table.add(e);
    }

template <typename T, typename U>
    void table_hachage<T,U>::supprimer(const T &cle){  

        int i=0;
        while( i< this->taille-1){
                table[i].suivant = NULL;
               delete this->table[i+1];
           }
        i++;
    }

template <typename T, typename U> 
    int const & Emplacement<T,U>::operator [] ( unsigned int const i ) const {
  return this->element[i];
}