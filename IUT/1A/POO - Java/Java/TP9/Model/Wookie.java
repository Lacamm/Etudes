
import java.util.*;

/**
 * 
 */
public class Wookie extends Personnage {

    /**
     * Default constructor
     */
    public Wookie(String Nom, Boolean Sexe, Integer Vie, Integer enfant) {
        super(Nom, Sexe, Vie, enfant);
        this.enfant = enfant;
    }

    /**
     * 
     */
    private Integer enfant;

}