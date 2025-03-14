import javafx.event.ActionEvent;
import javafx.event.EventHandler;

/* Contrôleur du bouton d'inscription' */

public class ActionInscription implements EventHandler<ActionEvent>{

    private Vue v;

    public ActionInscription(Vue v){
        this.v = v;
    }
    
    @Override
    public void handle(ActionEvent actionEvent){
        this.v.inscription();
    }
}