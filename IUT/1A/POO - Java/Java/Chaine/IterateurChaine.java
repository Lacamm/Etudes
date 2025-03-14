import java.util.Iterator;

public class IterateurChaine implements Iterator<Character>{

    private int pos, fin;
    private String chaine;

    public IterateurChaine(Chaine c){
        this.pos = 0;
        this.fin = c.getChaine().length();
        this.chaine = c.getChaine();
    }

    @Override
    public Character next(){
        Character res = this.chaine.charAt(this.pos);
        this.pos+=1;
        return res;
    }

    @Override
    public boolean hasNext(){return this.pos<this.fin;}
}