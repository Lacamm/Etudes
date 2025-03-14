import javafx.event.ActionEvent;
import javafx.event.EventHandler;

/* Contrôleur du bouton de retour lors de l'inscription */

public class ActionRetourInscription implements EventHandler<ActionEvent>{

    private Vue v;

    public ActionRetourInscription(Vue v){
        this.v = v;
    }
    
    @Override
    public void handle(ActionEvent actionEvent){
        this.v.retourInscription();
    }
}