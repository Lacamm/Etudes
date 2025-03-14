import java.util.Random;

public class Consumer implements Runnable {
    private final Drop drop;
    private final int id;
    private final Random r = new Random();

    public Consumer(int id, Drop drop) {
        this.id = id;
        this.drop = drop;
    }

    /*
    Consomme un produit et s'endort pour un temps aléatoire
     */
    public void run() {
        while(true){
            String product = drop.take();
            System.out.format("Consumer "+id+" read: %s%n", product);
            try{
                Thread.sleep(r.nextInt(30000));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
