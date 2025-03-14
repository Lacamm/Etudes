import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.control.Button;
import javafx.scene.control.Alert;

public class ActionButton implements  EventHandler<ActionEvent> {
    private CalculetteV2 appli;

    public ActionButton(CalculetteV2 appli) {
        this.appli = appli;
    }

    public void handle(ActionEvent actionEvent) {
        Button b = (Button) actionEvent.getSource();
        try {
            switch (b.getText()) {
                case "+":
                    this.appli.getResultat().setText("" + (Float.parseFloat(this.appli.getNombre1()) + Float.parseFloat(this.appli.getNombre2())));
                    break;
                case "-":
                    this.appli.getResultat().setText("" + (Float.parseFloat(this.appli.getNombre1()) - Float.parseFloat(this.appli.getNombre2())));
                    break;
                case "*":
                    this.appli.getResultat().setText("" + (Float.parseFloat(this.appli.getNombre1()) * Float.parseFloat(this.appli.getNombre2())));
                    break;
                case "/":
                    this.appli.getResultat().setText("" + (Float.parseFloat(this.appli.getNombre1()) / Float.parseFloat(this.appli.getNombre2())));
                    break;
            }
        }
        catch(NumberFormatException ex)
        {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("ERREUR !!!");
            alert.setHeaderText("Calcul impossible");
            alert.setContentText("Le format d'un des deux nombres est inconnu");
            alert.showAndWait();
        }
    }
}

