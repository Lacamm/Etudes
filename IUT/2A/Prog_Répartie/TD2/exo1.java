public class O {

    int m =100;

    public synchronized void m1( int id){

        System.out.println(" begin m1");
        for ( int i=0;i<m;i++){
            System.out.println (id+" m1 "+i);
        }
    System.out.println("end m1");
    }

    public synchronized void m2( int id){
        System .out. println (" begin m2");
        for ( int i=0;i<m;i++){
            System .out. println (id+" m2 "+i);
        }
        System.out.println ("end m2");
    }
}

class T1 extends Thread {
    O o;
    public T1(O o){
        this.o= o;
    }

    public void run(){
        o.m1 (1);
    }
}

class T2 extends Thread {
    O o;
    public T2(O o){
        this .o= o;
    }

    public void run (){
        o.m1 (2);
    }
}

public class Main{
    public static void main( String args []){
    O o = new O();
    T1 t1 = new T1(o);
    T2 t2 = new T2(o);
    t1.start ();
    t2.start ();
    }
}