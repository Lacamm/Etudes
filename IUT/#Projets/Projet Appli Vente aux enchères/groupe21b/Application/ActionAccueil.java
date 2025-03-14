import javafx.event.ActionEvent;
import javafx.event.EventHandler;

/* Contrôleur du bouton d'accueil */

public class ActionAccueil implements EventHandler<ActionEvent>{

    private Vue v;

    public ActionAccueil(Vue v){
        this.v = v;
    }
    
    @Override
    public void handle(ActionEvent actionEvent){
        this.v.accueil();
    }
}