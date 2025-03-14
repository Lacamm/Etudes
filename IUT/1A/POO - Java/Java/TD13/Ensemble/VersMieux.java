import java.util.*;

public class VersMieux<T> extends AbstractSet<T>{

    private List<T> listeInterne;
    private int nbElements ;

    public VersMieux(){
    // Remplissez listeInterne de 10000 cases à null
        this.listeInterne = new ArrayList<>();
        this.nbElements = 0;
        for (int n=0;n<10000;n++){
            this.listeInterne.add(null);
        }
    }

    public int size(){return this.nbElements;}
    public Iterator<T> iterator(){return new Iterateur<>(this.listeInterne);}

    public boolean add(T elem){
        int h  = (elem.hashCode()%10000 + 10000)%10000;
        if(this.listeInterne.get(h) == null){
            this.listeInterne.set(h,elem);
            this.nbElements+=1;
            return  true;
        }
        return false;
    }

    @Override
    public boolean contains(Object o){
         int h = (o.hashCode() % 10000 + 10000)%10000;
         return Objects.equals(this.listeInterne.get(h),o);
    }

}