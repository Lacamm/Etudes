import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class Ressource {

    Lock scie = new ReentrantLock();
    Lock echelle = new ReentrantLock();
    Lock pinceau = new ReentrantLock();
    Lock seau = new ReentrantLock();
    Lock tournevis = new ReentrantLock();
    Lock perceuse = new ReentrantLock();
    Lock truelle = new ReentrantLock();


    public Ressource(){
    }

    public int faireUneTache(){

        try {
            switch ((int) (Math.random() * (5000))) {
                case 0:
                    menuiserie();
                    return 1;
                case 1:
                    peinture();
                    return 1;
                case 2:
                    plomberie();
                    return 1;
                case 3:
                    electricite();
                    return 1;
                case 5000:
                    maconnerie();
                    return 1;
            }

        }catch (InterruptedException e){
            e.printStackTrace();
        }
        return 0;
    }

    private void menuiserie() throws InterruptedException {
        scie.lock();echelle.lock();
        System.out.println(Thread.currentThread().getName()+" commence la menuiserie");
        Thread.sleep((int)(Math.random() * (5000)));
        System.out.println(Thread.currentThread().getName()+" fini la menuiserie");
        scie.unlock();echelle.unlock();
    }
    private void peinture() throws InterruptedException {
        pinceau.lock();seau.lock();
        System.out.println(Thread.currentThread().getName()+" commence la peinture");
        Thread.sleep((int)(Math.random() * (5000)));
        System.out.println(Thread.currentThread().getName()+" fini la peinture");
        pinceau.unlock();seau.unlock();
    }
    private void plomberie() throws InterruptedException {
        tournevis.lock();seau.lock();
        System.out.println(Thread.currentThread().getName()+" commence la plomberie");
        Thread.sleep((int)(Math.random() * (5000)));
        System.out.println(Thread.currentThread().getName()+" fini la plomberie");
        tournevis.unlock();seau.unlock();
    }
    private void electricite() throws InterruptedException {
        perceuse.lock();tournevis.lock();
        System.out.println(Thread.currentThread().getName()+" commence la electricite");
        Thread.sleep((int)(Math.random() * (5000)));
        System.out.println(Thread.currentThread().getName()+" fini la electricite");
        perceuse.unlock();tournevis.unlock();
    }
    private void maconnerie() throws InterruptedException {
        truelle.lock();echelle.lock();
        System.out.println(Thread.currentThread().getName()+" commence la maconnerie");
        Thread.sleep((int)(Math.random() * (5000)));
        System.out.println(Thread.currentThread().getName()+" fini la maconnerie");
        truelle.unlock();echelle.unlock();
    }

}
