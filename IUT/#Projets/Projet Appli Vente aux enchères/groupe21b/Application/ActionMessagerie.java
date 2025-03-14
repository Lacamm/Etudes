import javafx.event.ActionEvent;
import javafx.event.EventHandler;

/* Contrôleur du bouton de messagerie */

public class ActionMessagerie implements EventHandler<ActionEvent>{

    private Vue v;

    public ActionMessagerie(Vue v){
        this.v = v;
    }
    
    @Override
    public void handle(ActionEvent actionEvent){
        this.v.messagerie();
    }
}