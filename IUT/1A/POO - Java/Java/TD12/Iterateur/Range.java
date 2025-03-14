import java.util.Iterator;
import java.lang.Iterable;

public class Range implements Iterable<Integer> {

    private int debut, limite, pas;

    public Range(int debut, int limite, int pas) {
        this.debut = debut;
        this.limite = limite;
        this.pas = pas;
    }

    public int getDebut(){return this.debut;}
    public int getFin(){return this.limite;}
    public int getPas(){return this.pas;}

    public Iterator<Integer> iterator(){return new IterateurSimple(this);}
}