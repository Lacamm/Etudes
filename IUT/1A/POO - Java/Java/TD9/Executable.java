import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.NoSuchElementException;

public class Executable {
    public static void afficheMin(List<Integer> liste){

        try{
            Integer minimum = Collections.min(liste);
            System.out.println("Ma liste: "+liste);
            System.out.println("Et voici le minimum: "+minimum);
        }
        catch (NoSuchElementException e){
            System.out.println("Ma liste: []");
            System.out.println("La liste est vide");
        }
    }


    public static void main (String [] args){
        List<Integer> liste = new ArrayList<>();
        System.out.println("Liste 1");
        afficheMin(liste);

        System.out.println("Liste 2");
        List<Integer> liste2 = new ArrayList<>();
        liste2.add(1);
        liste2.add(7);
        liste2.add(-2);
        afficheMin(liste2);
    }
}