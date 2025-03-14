import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.control.Alert;
import javafx.scene.control.ButtonType;
import javafx.scene.control.RadioButton;

import java.util.Optional;

/**
 * Controleur des radio boutons gérant le niveau
 */
public class ItemNiveau implements EventHandler<ActionEvent> {

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
	public ItemNiveau(MotMystere m, Pendu p) {
	    // A implémenter
	}

	/**
	 * gère le changement de niveau
	 * @param actionEvent
	 */
	@Override
	public void handle(ActionEvent actionEvent) {
	    // A implémenter
	}
}
