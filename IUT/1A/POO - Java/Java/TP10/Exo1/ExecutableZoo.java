import java.util.List;
import java.util.ArrayList;

public class ExecutableZoo{
    public static void main (String [] args){
        Animal g = new Animal("Sophie", false);
        Animal l = new Animal("Leo",true);

        Zoo z = new Zoo("Zoo");

        z.acceuillir(g);
        z.acceuillir(l);
        z.acceuillir(new Animal("Mowgli", true));

        
        try{z.soigner(l);}
        catch(AnimalPasPresentException e1){System.out.println("L'animal n'est pas présent dans le zoo");}
        catch(AnimalPasBlesseException e2){Syteme.out.println("L'animal n'est pas blessé");}
        
        try{z.soigner(g);}
        
    }
}