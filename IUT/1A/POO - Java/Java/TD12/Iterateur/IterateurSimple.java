import java.util.Iterator;

public class IterateurSimple implements Iterator<Integer> {

    private int pos;
    private int fin;
    private int pas;

    public IterateurSimple(Range r) {
        this.pos = r.getDebut();
        this.fin = r.getFin();
        this.pas = r.getPas();
        }

    public Integer next(){
        Integer res = this.pos;
        this.pos+=this.pas;
        return res;
        }

    public boolean hasNext(){
        return this.pos<this.fin;
        }
}