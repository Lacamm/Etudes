public class ProducerConsumerExample {
    public static void main(String[] args) {
        Drop drop = new Drop();
	    Producer p = new Producer(0, drop);
	    Consumer c = new Consumer(0, drop);
        (new Thread(p)).start();
        (new Thread(c)).start();
   }
}
