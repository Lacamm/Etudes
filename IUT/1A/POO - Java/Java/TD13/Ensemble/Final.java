import java.util.*;

class Final<T> extends AbstractSet<T> {

    private List<List<T>> listeInterne;
    private int nbElements;

    public Final(){
        this.nbElements = 0;
        this.listeInterne = new ArrayList<>();
        for (int i=0; i<10000;i++){
            listeInterne.add(new ArrayList<>());
        }
    }
    public int size(){return this.nbElements;}
    public Iteator<T> iterator(){return new IterateurF<>(this.listeInterne);}

    public boolean add(T elem){
        if(elem == null){return false;}

        int h  = (elem.hashCode()%10000 +10000)%10000;
        
        if(!this.listeInterne.get(h).contains(elem)){
            this.listeInterne.get(h).add(elem);
            ++this.nbElements;
            return  true;
        }
        return false;
    }

    @Override
    public boolean contains(Object o){
        if(o == null){return false;}
        int h = (o.hashCode() % 10000 + 10000)%10000;
        return Objects.equals(this.listeInterne.get(h),o);
    }
}
