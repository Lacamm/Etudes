public class Assembleur extends Thread{


	Stock stock;
	public Assembleur(Stock stock){
	this.stock = stock;

	}


	public void run(){
	try{
	while(true){

		stock.getMoteur();
		stock.getCarrosserie();
		stock.getRoues();
		try{
		Thread.sleep(20000);
		}
		catch(Exception e){e.printStackTrace();}	
		System.out.println("Voiture assemblée");
	}
	}catch(Exception e){e.printStackTrace();}

	}	




}
