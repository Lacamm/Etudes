import javafx.event.ActionEvent;
import javafx.event.EventHandler;

/* Contrôleur du bouton des enchères */

public class ActionEncheres implements EventHandler<ActionEvent>{

    private Vue v;

    public ActionEncheres(Vue v){
        this.v = v;
    }
    
    @Override
    public void handle(ActionEvent actionEvent){
        this.v.encheres();
    }
}