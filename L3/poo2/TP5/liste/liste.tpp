template< typename T >
Liste<T>::Liste() {
    this->tete = NULL;
    this->queue = NULL;
    this->taille = 0;
}

template< typename T >
Liste<T>::Liste(T _valeur) {
    Noeud<T> * n = new Noeud<T>(_valeur);
    taille = 1;
    tete = n;
    queue = n;
}

template< typename T >
Liste<T>::~Liste() {
    Noeud<T> * n = tete;
    Noeud<T> * suivant = tete;
    while(n != NULL){
        suivant = n->suivant;
        n->suivant = NULL;
        delete n;
        n=suivant;
    }
}

template< typename T >
void Liste<T>::ajouter_fin(T _valeur) {
    Noeud<T> * n = new Noeud<T>(_valeur);

    if(this->taille==0) {
        this->tete = n;
        this->queue = this->tete;
    }
    else{ 
        queue->suivant=n;
        queue=n;
    }
    ++this->taille;
}

template< typename T >
void Liste<T>::supprimer_fin() {
    assert(this->taille > 0);
    Noeud<T> * n = tete;
    while(n->suivant != queue){
        n = n->suivant;
    }
    n->suivant = NULL;
    delete queue;
    queue = n;
    taille--;
}

template< typename T >
T& Liste<T>::operator[](size_t i) {
    assert(i>=0 && i < this->taille);
    Noeud<T> * n = tete;
    for(size_t l=0; l<i; l++){
        n=n->suivant;
    }
    return n->valeur;
}

/* Hypothèse : T n'est pas un pointeur */
template< typename T >
std::ostream& operator<<(std::ostream &os, const Liste<T> &l) {
    struct Noeud<T> *parcours = l.tete;
    Noeud<T> * n = l.tete;
    while(n != NULL){
        os << n->valeur;
        n = n->suivant;
    }
    return os;
}
