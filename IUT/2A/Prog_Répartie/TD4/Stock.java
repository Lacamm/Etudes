import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.Condition;

public class Stock {
    final int NBROUES = 20;
    final int NBMOTEURS = 5;
    final int NBCARROSSERIE = 3;

    int roues;
    int moteur;
    int carrosserie;

    Lock lockMoteur;
    Lock lockRoues;
    Lock lockCarro;

    Condition condiMoteur;


    public Stock(){
        lockMoteur = new ReentrantLock();
        lockCarro = new ReentrantLock();
        lockRoues = new ReentrantLock();

        condiMoteur = lockMoteur.getCondition();
    }

    public void addMoteur() throws InterruptedException{
        lockMoteur.lock();

        while(moteur<=NBMOTEURS){            
            condiMoteur.await();
        }
        
        moteur++;
        System.out.println("MOTEUR ajouté \t Stock MOTEUR \t = "+moteur);

        condiMoteur.signal();

        lockMoteur.lock();
    }

    public void getMoteur(){
        lockMoteur.lock();

        while(moteur<=0){            
            condiMoteur.await();
        }
        
        moteur--;
        System.out.println("MOTEUR ajouté \t Stock MOTEUR \t = "+moteur);

        condiMoteur.signal();

        lockMoteur.lock();
    }

    public void addRoues() throws InterruptedException{
        lockRoues.lock();

        System.out.println("ROUES ajouté \t Stock ROUES \t = "+roues);
        lockRoues.lock();
    }

    public void addCarrosserie() throws InterruptedException{
        lockCarro.lock();

        System.out.println("CARROSSERIE ajouté \t Stock CARROSSERIE \t = "+carrosserie);
        lockCarro.lock();
    }

    public static void main (String [] args){
        Stock stock = new Stock();



    }
}
