import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.control.Alert;
import javafx.scene.control.*;

/* Contrôleur du bouton de validation lors de la connexion */

public class ActionValiderConnexion implements EventHandler<ActionEvent>{

    private Vue v;

    public ActionValiderConnexion(Vue v){
        this.v = v;
    }
    
    @Override
    public void handle(ActionEvent actionEvent){
        if(! this.v.connexionValide()){
            Alert alert = new Alert(Alert.AlertType.NONE);
            alert.setHeaderText("Attention");
            alert.setContentText("Login ou mot de passe incorrect!");
            ButtonType ok = new ButtonType("Ok");
		    alert.getButtonTypes().addAll(ok);
		    alert.showAndWait();
        }
        else{this.v.validerInscription();}
    }
}