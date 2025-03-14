template < typename T > T maximum(const T &a, const T &b) {
    return a < b ? a : b; //surchager < pour des types plus complexes
    //constructeur par copie car on retourne des "objets"
}

template <typename T> T somme(const vector<T> &v){
    T res = T();
    for(unsigned int i=0; i<v.size(); i++){
        res=res+v[i];
    }
    return res;
}

template <typename T> vector<T> tri_panier(const vector<T> &v){
    vector<T> trie;
    map<T,int> panier;
    typename map<T,int>::iterator it;

    for(unsigned int i=0; i<v.size();i++){
        panier[v[i]] = panier[v[i]] + 1;
    }
    for( it = panier.begin(); it!=panier.end(); it++){
        for(unsigned int j=0; j<it->second; j++){
            trie.push_back(it->first);
        }
    }
    return trie;
}