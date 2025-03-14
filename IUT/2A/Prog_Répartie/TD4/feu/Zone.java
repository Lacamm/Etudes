import java.util.concurrent.CyclicBarrier;

public class Zone {
    int width;
    int height;
    int[][] current;
    int[][] next;
    int nbThreads;
    boolean hasChanged;
    CyclicBarrier barrier;

    public Zone(int width, int height){
        this.width = width;
        this.height = height;
        nbThreads = Runtime.getRuntime().availableProcessors();
        barrier = new CyclicBarrier(nbThreads);
        hasChanged = true;
        //initialiser des cases avec du feu ou à 0
    }

    public void propagation(int i, int j) {
        if (current[i][j] == 0) {
            int sum = 0;
            for (int n = i - 1; n <= i + 1; ++n) {
                if (0 < n && n < this.width) {
                    for (int m = j - 1; m <= j + 1; ++m) {
                        if (0 < m && m < this.height) {
                            sum += current[n][m];
                        }
                    }
                }
            }
            if (sum >= 6)
                next[i][j] = 1;
        }
        else if(current[i][j] >= 4){}
        else
            next[i][j] += 1;

        if (current[i][j] != next[i][j])
            sync(true);
    }

    public synchronized void sync(boolean bool) {
        hasChanged = bool;
    }

    @Override
    public String toString(){

        String res = "";

        for (int n = 0; n < this.height; ++n) {
            for (int m = 0; m < this.width; ++m) {
                res += current[n][m] + ' ';
            }
            res += '\n';
        }
        return res;
    }

    public static void main(String [] args){
        int w = Integer.parseInt(args[0]);
        int h = Integer.parseInt(args[1]);
        Zone zone = new Zone(w,h);

        int linepaththread = zone.height/zone.nbThreads;
        T[] threads = new T[zone.nbThreads];
        for(int i=0; i<zone.nbThreads; i++){
            int start = i*linepaththread;
            int end = start + linepaththread;
            if(i==zone.nbThreads-1)
                end=zone.height;
            threads[i] = new T(zone,start,end);
            threads[i].start();
        }
    }
}
