
import java.util.*;

/**
 * 
 */
public class Ewok extends Personnage {

    /**
     * Default constructor
     */
    public Ewok(String Nom, Boolean Sexe, Integer Vie, String couleur) {
        super(Nom,Sexe,Vie);
        this.couleur = couleur;
    }

    /**
     * 
     */
    private String couleur;

    public void attaque(Personnage p, Integer degats){
        Integer v = p.getVie();
        v = v-degats;
        p.setVie();
    }

}