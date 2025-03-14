import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.control.Alert;
import javafx.scene.control.*;

/* Contrôleur du bouton de validation lors de l'inscription */

public class ActionValiderInscription implements EventHandler<ActionEvent>{

    private Vue v;

    public ActionValiderInscription(Vue v){
        this.v = v;
    }
    
    @Override
    public void handle(ActionEvent actionEvent){
        if(! this.v.inscriptionValide()){
            Alert alert = new Alert(Alert.AlertType.NONE);
            alert.setHeaderText("Attention");
            alert.setContentText("Un ou plusieurs champs sont incorrects!");
            ButtonType ok = new ButtonType("Ok");
		    alert.getButtonTypes().addAll(ok);
		    alert.showAndWait();
        }
        else{this.v.validerInscription();}
    }
}