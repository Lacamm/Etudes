import java.util.concurrent.CyclicBarrier;
import java.util.ArrayList;

public class Main {
    CyclicBarrier cb;
    Ressource r = new Ressource();

    public static ArrayList<Piece> listePiece;

    public void travaux(int ouvrier, int piece) {
        cb = new CyclicBarrier(ouvrier);
        ArrayList<Piece> listePiece = new ArrayList<>();

        for (int i = 0; i < ouvrier; ++i) {
            Ouvrier o = new Ouvrier(r, cb);
            o.start();
        }

        for (int i = 0; i < piece; ++i){
            Piece p = new Piece(i);
            listePiece.add(p);
        }
    }

    public static int getNbPiece(){return listePiece.size();}
    public static ArrayList<Piece> getPiece(){return listePiece;}


    public static void main(String[] args) {

        Main chantier = new Main();

        chantier.travaux(3, 4);
    }
}
