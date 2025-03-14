import java.util.*;

public class Iterateur<T> implements Iterator<T>{

    private List<T> valeurs;
    private int position;
    private int lastPosition;

    public Iterateur(List<T> array){
      this.position = 0;
      this.lastPosition = -1;
      this.valeurs = array;
      while(this.position < this.valeurs.size() && this.valeurs.get(this.position) == null){
        ++this.position;
      }
    }

    @Override
    public T next(){
      this.lastPosition = this.position;
      T valeur = this.valeurs.get(this.position++);
      while (this.valeurs.size() > this.position  && this.valeurs.get(this.position) == null){
        ++this.position;
      }
      return valeur;
    }

    @Override
    public boolean hasNext(){
        return this.position < this.valeurs.size();
      }

    @Override
    public void remove(){
        this.valeurs.remove(this.lastPosition);
    }
}