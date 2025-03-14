import java.util.concurrent.BrokenBarrierException;
import java.util.concurrent.CyclicBarrier;

public class Ouvrier extends Thread implements Runnable{

    private Ressource r;
    private int nbTache;
    private CyclicBarrier cb;

    public Ouvrier(Ressource r, CyclicBarrier cb){
        this.r = r;
        this.nbTache = 0;
        this.cb=cb;
    }

    @Override
    public void run() {
        while (this.nbTache < 3) {
            this.nbTache += this.r.faireUneTache(this);
        }
        try {
            this.cb.await();
        } catch (InterruptedException | BrokenBarrierException e) {
            e.printStackTrace();
        }
    }

    @Override
    public String toString() {
        return Thread.currentThread().toString();
    }
}
