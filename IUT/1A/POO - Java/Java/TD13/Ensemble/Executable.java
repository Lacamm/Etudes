import java.util.Set;

public class Executable{
    public static void main(String [] args){

        // Set<Integer> e1 = new EnsembleInefficace<>();
        // System.out.println(e1);
        // e1.add(6);
        // e1.add(-4);
        // e1.add(92);
        // System.out.println(e1.size());
        // for (Integer elem: e1){System.out.println(elem);}
        // System.out.println(e1);


        Set<Integer> e2 = new VersMieux<>();
        e2.add(5);
        e2.add(5);
        e2.add(4546);
        e2.add(7);
        e2.add(5);
        e2.add(7);
        e2.add(6);
        System.out.println(e2);
        e2.remove(6);
        System.out.println(e2);
    }
}