public class exo2_thread {
    public static void main(String args[]) throws InterruptedException {

        int A[][] = { { 1, 2 }, { 3, 4 } };
        int B[][] = { { 5, 6 }, { 7, 8 } };

        int C[][] = new int[2][2];

        T1 t1 = new T1();
        T2 t2 = new T2();
        t1.start();
        t2.start();
        t1.join();
    }
}


public class T1 extends Thread{
    public void run(){
        //TO DO
    }
}

public class T2 extends Thread{
    public void run(){
        //TO DO
    }
}