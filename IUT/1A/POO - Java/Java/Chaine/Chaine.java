import java.util.Iterator;
import java.lang.Iterable;

public class Chaine implements Iterable<Character>{

    private String chaine;

    public Chaine(String s){this.chaine = s;}

    public String getChaine(){return this.chaine;}
    public int getLength(){return c.length();}

    public Iterator<String> iterator(){return new IterateurChaine(this);}
}