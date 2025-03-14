import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.lang.Thread;

class tab{
    public int [] tab = {1,2,3,-3,4,1,9,8,9,-2};
    public int x,y;

    Lock lx = new ReentrantLock();
    Lock ly = new ReentrantLock();

    public void addX(int n){
        lx.lock();
        x = x+n;
        lx.unlock();
    }

    public void addY(int n){
        ly.lock();
        y = y+n;
        ly.unlock();
    }


    public static void main(String [] args){
        tab Tab = new tab();
        Thread t1 = new Thread(Tab,0,5);
        Thread t2 = new Thread(Tab,5,10);

        t1.start();
        t2.start();
        
        try{
            t1.join();
            t2.join();
        }

        catch (Exception e) {
            
        }



    }
}