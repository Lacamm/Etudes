public class Main{
	public static void main(String  args[]){
        Serveur serveur = new Serveur();

        Client c1 = new Client("Pierre", serveur);
        Client c2 = new Client("Paul", serveur);
        Client c3 = new Client("Jacques", serveur);

        c1.start();
        c2.start();
        c3.start();
	}
}