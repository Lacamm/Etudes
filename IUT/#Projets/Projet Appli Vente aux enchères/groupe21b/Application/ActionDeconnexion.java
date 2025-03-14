import javafx.event.ActionEvent;
import javafx.event.EventHandler;

/* Contrôleur du bouton de déconnexion */

public class ActionDeconnexion implements EventHandler<ActionEvent>{

    private Vue v;

    public ActionDeconnexion(Vue v){
        this.v = v;
    }
    
    @Override
    public void handle(ActionEvent actionEvent){
        this.v.deconnexion();
    }
}