import java.util.concurrent.BrokenBarrierException;

public class T extends Thread{
    Zone zone;
    int start;
    int end;

    public T(Zone zone, int start, int end){
        this.zone = zone;
        this.start = start;
        this.end = end;
    }

    public void run() {
        while (zone.hasChanged) {
            System.out.println("sync");
            if (start == 0){
                zone.sync(false);                
            }

            try {
                zone.barrier.await();
            } catch (InterruptedException | BrokenBarrierException e) {
                e.printStackTrace();
            }
            System.out.println("propa");
            for (int i = start; i < end; i++) {
                for (int j = 0; j < zone.width; ++j) {
                    zone.propagation(i, j);
                }
            }
            try {
                zone.barrier.await();
            } catch (InterruptedException | BrokenBarrierException e) {
                e.printStackTrace();
            }
            System.out.println("affichage");
            if (start == 0) {
                System.out.println(zone.toString());
            }
            System.out.println("remplacement matrices");
            zone.current = zone.next;
            zone.next = new int[zone.height][zone.width];

            try {
                zone.barrier.await();
            } catch (InterruptedException | BrokenBarrierException e) {
                e.printStackTrace();
            }
        }
    }
}