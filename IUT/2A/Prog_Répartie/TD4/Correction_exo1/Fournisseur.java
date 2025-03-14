import java.util.Random;

class Fournisseur extends Thread{

	int type;

	Stock stock;

	public Fournisseur(int type,Stock stock){
	this.type = type;
	this.stock =stock;
	}


	public void run(){
	Random rand = new Random();
	while(true){

		try{
		if (type==1){
		stock.addRoues();
		
		}
		else if (type==2){
		stock.addMoteur();
		
		}
		else{
		stock.addCarrosserie();
		
		}

		Thread.sleep(rand.nextInt(10)*1000);
		}
		catch(Exception e){e.printStackTrace();}

	}
	
	}



}
