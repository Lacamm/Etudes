import java.util.ArrayList;

public class Main{

    public static void main(String[] args) throws InterruptedException {
        
        ArrayList<Integer> vals1 = new ArrayList<>();
        vals1.add(1);
        vals1.add(2);
        vals1.add(3);
        vals1.add(4);
        ArrayList<Integer> vals2 = new ArrayList<>();
        vals2.add(5);
        vals2.add(6);
        vals2.add(7);
        vals2.add(8);

        Matrice m1 = new Matrice(vals1, 2);
        Matrice m2 = new Matrice(vals2, 2);

        System.out.println(m1.multiplier(m2));

    }
}