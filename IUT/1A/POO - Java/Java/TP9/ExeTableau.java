import java.util.NoSuchElementException;
import java.util.Collections;


public class ExeTableau{

    public static void main (String [] args){

        Tableau tab1 = new Tableau();     
        tab1.remplir();     

        try{System.out.println("Min: "+Collections.min(tab1.getContenu()));}
        catch(NoSuchElementException e){System.out.println("Il n’y a pas de minimum: le tableau est vide !");}

        try{System.out.println("Valeur pour l'indice: "+tab1.get(1));}
        catch(NoSuchElementException e){System.out.println("L'indice n'est pas compris dans le tableau");}

        try{System.out.println("Max: "+tab1.getMax());}
        catch(NoSuchElementException e){System.out.println("Il n’y a pas de maximum: le tableau est vide !");}
    }
}