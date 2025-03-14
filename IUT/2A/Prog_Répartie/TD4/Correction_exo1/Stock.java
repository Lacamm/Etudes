import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.Condition;

public class Stock{

	final int NBROUES = 20;
	final int NBMOTEUR = 5;
	final int NBCARROSSERIE = 3;

	int carrosserie;
	int roues;
	int moteur;

	Lock lockMoteur;
	Lock lockCarro;
	Lock lockRoues;

	Condition condMoteurFull;
	Condition condMoteurEmpty;

	Condition condRouesFull;
	Condition condRouesEmpty;

	Condition condCarroFull;
	Condition condCarroEmpty;


	public Stock(){
		lockMoteur = new ReentrantLock();
		lockCarro = new ReentrantLock();
		lockRoues = new ReentrantLock();
		condMoteurFull = lockMoteur.newCondition();
		condMoteurEmpty = lockMoteur.newCondition();

		condRouesFull = lockRoues.newCondition();
		condRouesEmpty = lockRoues.newCondition();

		condCarroFull = lockCarro.newCondition();
		condCarroEmpty = lockCarro.newCondition();
	}


	public void addMoteur() throws InterruptedException{
		lockMoteur.lock();
		while(moteur>=NBMOTEUR){
			condMoteurFull.await();
		}
		moteur +=1;
		System.out.println("MOTEUR ajouté \t Stock MOTEUR \t="+moteur);
		condMoteurEmpty.signal();
		lockMoteur.unlock();
	}

	public void getMoteur() throws InterruptedException{
		lockMoteur.lock();
		while(moteur==0){
			condMoteurEmpty.await();
		}
		moteur -=1;
		System.out.println("MOTEUR \t retiré  Stock MOTEUR \t="+moteur);
		condMoteurFull.signal();
		lockMoteur.unlock();
	}


	public void addCarrosserie() throws InterruptedException{
		lockCarro.lock();
		while(carrosserie>=NBCARROSSERIE){
			condCarroFull.await();
		}
		carrosserie +=1;
		System.out.println("CARROSSERIE \t ajouté \t Stock CARROSSERIE \t="+carrosserie);
		condCarroEmpty.signal();
		lockCarro.unlock();
	}

	public void getCarrosserie() throws InterruptedException{
		lockCarro.lock();
		while(carrosserie==0){
			condCarroEmpty.await();
		}
		carrosserie -=1;
		System.out.println("CARROSSERIE \t retiré Stock CARROSSERIE \t="+carrosserie);
		condCarroFull.signal();
		lockCarro.unlock();
	}


	public void addRoues() throws InterruptedException{
		lockRoues.lock();
		while(roues>=NBROUES){
			condRouesFull.await();
		}
		roues +=1;
		System.out.println("ROUE \t ajoutée  Stock ROUE \t="+roues);
		if (roues>=4)
		condRouesEmpty.signal();
		lockRoues.unlock();
	}

	public void getRoues() throws InterruptedException{
	    /*lockRoues.lock();
		while(roues<4){
			condRouesEmpty.await();
		}
		System.out.println("4 ROUES retirées \t Stock ROUE \t="+roues);
		roues -=4;
		condRouesFull.signal();
		lockRoues.unlock();
	    */
	    getRoues(4);
	}

	public void getRoues(int nbR) throws InterruptedException{
		lockRoues.lock();
		while(roues<nbR){
			condRouesEmpty.await();
		}
		System.out.println(nbR+" ROUES retirées \t Stock ROUE \t="+roues);
		roues -=nbR;
		condRouesFull.signal();
		lockRoues.unlock();
	}

    
}
