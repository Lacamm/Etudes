import javafx.animation.Animation;
import javafx.animation.KeyFrame;
import javafx.animation.Timeline;
import javafx.scene.control.Label;
import javafx.util.Duration;

/**
 * Permet de gérer un label associé à une Timeline pour afficher un temps écoulé
 */
public class Chronometre extends Label{
    /**
     * timeline qui va gérer le temps
     */
    private Timeline timeline;
    /**
     * la fenêtre de temps
     */
    private KeyFrame keyFrame;
    /**
     * le contrôleur associé au chronomètre
     */
    private ActionTemps actionTemps;

    /**
     * Constructeur permettant de créer le chronomètre
     * avec un label initialisé à "0:0:0"
     * Ce constructeur créer la Timeline, la KeyFrame et le contrôleur
     */
    Chronometre(){
	// A implémenter
    }

    /**
     * Permet au controleur de mettre à jour le label
     * la durée est affichée sous la forme h:m:s
     * @param tempsMillisec la durée depuis à afficher
     */
    public void setTime(long tempsMillisec){
	// A implémenter
    }

    /**
     * Permet de démarrer le chronomètre
     */
    public void start(){
        // A implémenter
    }

    /**
     * Permet d'arrêter le chronomètre
     */
    public void stop(){
        // A implémenter
    }

    /**
     * Permet de remettre le chronomètre à 0
     */
    public void resetTime(){
        // A implémenter
    }
}
