import javafx.event.ActionEvent;
import javafx.event.EventHandler;

/* Contrôleur du bouton de vendre */

public class ActionVendre implements EventHandler<ActionEvent>{

    private Vue v;

    public ActionVendre(Vue v){
        this.v = v;
    }
    
    @Override
    public void handle(ActionEvent actionEvent){
        this.v.vendre();
    }
}