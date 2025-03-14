public class ProducerConsumerExample {
    public static void main(String[] args) {
        Drop drop = new Drop();
	    Producer p = new Producer(0, drop);
        Consumer c = new Consumer(0, drop);
        Consumer c1 = new Consumer(1, drop);
        Consumer c2 = new Consumer(2, drop);
        (new Thread(p)).start();
        (new Thread(c)).start();
        (new Thread(c1)).start();
        (new Thread(c2)).start();
   }
}
