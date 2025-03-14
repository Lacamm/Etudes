import java.util.List;
import java.util.ArrayList;

public class ExecutableMax{

    public static void main (String [] args){
        List<Integer> liste1 = new ArrayList<>();
        List<Integer> liste2 = new ArrayList<>();
        List<Integer> liste3 = new ArrayList<>();

        List<List<Integer>> listeP = new ArrayList<>(); 

        liste1.add(1);
        liste1.add(3);
        liste1.add(2);

        liste2.add(2);
        liste2.add(10);
        liste2.add(1);

        liste3.add(1);
        liste3.add(100);
        liste3.add(3);
        liste3.add(2);
        liste3.add(4);

        listeP.add(liste1);
        listeP.add(liste2);
        listeP.add(liste3);      

        System.out.println(bibMax.sommeMax(listeP));
    }
}