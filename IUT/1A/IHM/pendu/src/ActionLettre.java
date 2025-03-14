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
	    this.m = m;
	    this.p = p;
	}

    /**
     * Actions à effectuer lors du clic sur une touche du clavier
     * Il faut donc: Essayer le lettre, mettre à jour l'affichage et vérifier si la partie est finie
     * @param actionEvent l'événement
     */
	@Override
	public void handle(ActionEvent actionEvent) {
		Button bout = (Button) actionEvent.getTarget();
		String lettre = bout.getText();
		this.m.essaiLettre(lettre.charAt(0));
		this.p.majAffichage();

		if (this.m.perdu() || this.m.gagne()) {
			this.p.getChrono().stop();
			Alert al = new Alert(Alert.AlertType.INFORMATION);

			if (this.m.perdu()) {
				al.setTitle("Raté ...");
				al.setHeaderText("Vous avez perdu, le mot était : " + m.getMotATrouve());
				al.setContentText("Votre temps est de : " + this.p.getChrono().getText());
			}
			else {
				al.setTitle("FELICITATIONS !!!");
				al.setHeaderText("Vous avez gagné, vous avez trouvé le mot : " + m.getMotATrouve());
				al.setContentText("Votre temps est de : " + this.p.getChrono().getText());
			}
			al.showAndWait();
			this.p.activerNiveau(true);
		}
	}
}
