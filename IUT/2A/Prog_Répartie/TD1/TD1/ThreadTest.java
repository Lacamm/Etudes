import java.util.ArrayList;

public class ThreadTest extends Thread {
    private ArrayList<Multiplication> multiplications;
    
    public ThreadTest(){
        this.multiplications = new ArrayList<>();
    }
    public void run(){
        for (Multiplication m: this.multiplications){
            m.multiplier();
        }
    }
    public void ajoutMultiplication(Multiplication m){
        this.multiplications.add(m);
    }
}
