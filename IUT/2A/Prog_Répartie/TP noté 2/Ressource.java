import java.util.ArrayList;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.ArrayList;

public class Ressource {

    Lock scie = new ReentrantLock();
    Lock echelle = new ReentrantLock();
    Lock pinceau = new ReentrantLock();
    Lock truelle = new ReentrantLock();
    Lock seau = new ReentrantLock();
    ArrayList<Piece> listePiece;

    public Ressource(){
        this.listePiece = Main.getPiece();
    }

    public int faireUneTache(Ouvrier o){

        try {
            if (Thread.currentThread().getId()-9 == 0){
                menuiserie();
                return 1;
            }
            else if (Thread.currentThread().getId()-9 == 1){
                peinture();
                return 1;
            }
            else if (Thread.currentThread().getId()-9 == 2){
                maconnerie();
                return 1;
            }
        }
        catch (InterruptedException e){
            e.printStackTrace();
        }
        return 0;
    }

    private void menuiserie() throws InterruptedException {
        scie.lock();echelle.lock();
        System.out.println("Ouvrier "+ (Thread.currentThread().getId()-9) +" commence la menuiserie");
        Thread.sleep((int)(Math.random() * (5000)));
        System.out.println("Ouvrier "+ (Thread.currentThread().getId()-9) +" fini la menuiserie");
        scie.unlock();echelle.unlock();
    }
    private void peinture() throws InterruptedException {
        pinceau.lock();seau.lock();
        System.out.println("Ouvrier "+ (Thread.currentThread().getId()-9) +" commence la peinture");
        Thread.sleep((int)(Math.random() * (5000)));
        System.out.println("Ouvrier "+ (Thread.currentThread().getId()-9) +" fini la peinture");
        pinceau.unlock();seau.unlock();
    }
    
    private void maconnerie() throws InterruptedException {
        truelle.lock();echelle.lock();
        System.out.println("Ouvrier "+ (Thread.currentThread().getId()-9) +" commence la maconnerie");
        Thread.sleep((int)(Math.random() * (5000)));
        System.out.println("Ouvrier "+ (Thread.currentThread().getId()-9) +" fini la maconnerie");
        truelle.unlock();echelle.unlock();
    }

}
