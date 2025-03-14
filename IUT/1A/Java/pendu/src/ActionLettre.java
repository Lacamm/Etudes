import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;

/**
 * Controleur du clavier
 */
public class ActionLettre implements EventHandler<ActionEvent> {

    /**
     * modèle du jeu
     */
	private MotMystere m;
	/**
	 * vue du jeu
     */
	private Pendu p;

    /**
     * @param m modèle du jeu
     * @param p vue du jeu
     */
	ActionLettre(MotMystere m, Pendu p){
	    // A implémenter
	}

    /**
     * Actions à effectuer lors du clic sur une touche du clavier
     * Il faut donc: Essayer le lettre, mettre à jour l'affichage et vérifier si la partie est finie
     * @param actionEvent l'événement
     */
	@Override
	public void handle(ActionEvent actionEvent) {
	    // A implémenter
	}
}
