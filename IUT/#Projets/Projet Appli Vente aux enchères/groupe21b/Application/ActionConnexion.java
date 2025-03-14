import javafx.event.ActionEvent;
import javafx.event.EventHandler;

/* Contrôleur du bouton de connexion */

public class ActionConnexion implements EventHandler<ActionEvent>{

    private Vue v;

    public ActionConnexion(Vue v){
        this.v = v;
    }
    
    @Override
    public void handle(ActionEvent actionEvent){
        this.v.connexion();
    }
}