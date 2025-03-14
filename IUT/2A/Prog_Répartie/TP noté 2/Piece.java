import java.util.ArrayList;

public class Piece {
    
    private int id;
    private ArrayList<Ouvrier> listeOuvrier;

    public Piece(int id){
        this.id = id;
        this.listeOuvrier = new ArrayList<>();
    }

    public int getId(){return this.id;}

    public ArrayList<Ouvrier> getListeOuvrier(){return this.listeOuvrier;}

    public Boolean isPieceEmpty(){return this.listeOuvrier.isEmpty();}

    public void ajouterOuvrier(Ouvrier o){this.listeOuvrier.add(o);}

    public void retirerOuvrier(Ouvrier o){this.listeOuvrier.remove(o);}
}
