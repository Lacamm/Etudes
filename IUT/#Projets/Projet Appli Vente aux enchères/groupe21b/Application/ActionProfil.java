import javafx.event.ActionEvent;
import javafx.event.EventHandler;

/* Contrôleur du bouton de profil */

public class ActionProfil implements EventHandler<ActionEvent>{

    private Vue v;

    public ActionProfil(Vue v){
        this.v = v;
    }
    
    @Override
    public void handle(ActionEvent actionEvent){
        this.v.profil();
    }
}