import java.util.ArrayList;
public class EnsembleChaines {
    ArrayList<ChainePositionnee> chaines;
    public EnsembleChaines(){chaines= new ArrayList<ChainePositionnee>(); }

    public void ajouteChaine(int x, int y, String c){
        chaines.add(new ChainePositionnee(x,y,c));}

    public void union(EnsembleChaines e){
        for(ChainePositionnee c : e.chaines)
            chaines.add(c);
    }


    public boolean contient(int posx, int posy){
        for(ChainePositionnee c: chaines){
            if (c.x<=posx  && c.y == posy && posx < c.x+c.c.length())
                return true;
        }
        return false;

    }
    public void vider(){ chaines.clear();}
}
