import java.util.*;

public class IterateurF<T> implements Iterator<T>{

    private List<List<T>> valeurs;
    private Iterator<T> iterActuel; // Itérteur des sous-listes
    private Iterator<List<T>> iterListe; // Itérateur des elem des sous-listes
    

    public IterateurF(List<List<T>> liste){
        this.valeurs = liste;
        this.iterListe = this.valeurs.iterator();
        this.iterActuel = this.iterListe.next().iterator();
    }

    @Override
    public T next(){
        while (!iterActuel.hasNext()){
            this.iterActuel = iterListe.next().iterator();
        }
        return this.iterActuel.next();
    }

    @Override
    public boolean hasNext(){
        while(!this.iterActuel.hasNext() && this.iterListe.hasNext()){
            this.iterActuel = this.iterListe.next().iterator();
        }
        return this.iterActuel.hasNext();
    }

    // @Override
    // public void remove(){
    //     this.valeurs.remove(this.iterActuel);
    // }
}