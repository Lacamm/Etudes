import java.util.List;
import java.util.ArrayList;
import java.util.AbstractSet;
import java.util.Iterator;

public class EnsembleInefficace<T> extends AbstractSet<T>{

    private List<T> listeInterne;

    public EnsembleInefficace(){this.listeInterne = new ArrayList<>();}

    public int size(){return this.listeInterne.size();}
    public Iterator<T> iterator(){return this.listeInterne.iterator();}
    public boolean add(T elem){return this.listeInterne.add(elem);}

}