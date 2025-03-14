import java.util.Random;

public class Producer implements Runnable {
    private final Drop drop;
    private final int id;
    private final Random r = new Random();

    private final static String[] products = {
            "Mares eat oats",
            "Does eat oats",
            "Little lambs eat ivy",
            "A kid will eat ivy too"
    };

    public Producer(int id, Drop drop) {
        this.id = id;
        this.drop = drop;
    }

    /*
    Ajoute un produit (aléatoire) à interval régulier
     */
    public void run() {
        while(true){
            String product = products[r.nextInt(products.length)];
            drop.put(product);
            System.out.println("Producer "+id+" a ajouté : "+product);
            try {
                Thread.sleep(5000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
