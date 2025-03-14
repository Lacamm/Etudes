import java.util.concurrent.CyclicBarrier;

public class Main {
    CyclicBarrier cb;
    Ressource r = new Ressource();

    public void play(int ouvrier){
        cb = new CyclicBarrier(ouvrier);
            for (int i = 0; i < ouvrier; i++){
                Ouvrier o = new Ouvrier(r, cb);
                o.start();
            }
    }


    public static void main(String[] args) {

        Main chantier = new Main();
            chantier.play(4);
    }
}
