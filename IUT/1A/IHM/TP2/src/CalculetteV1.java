import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.TextField;
import javafx.scene.control.Label;
import javafx.scene.control.Button;
import javafx.scene.layout.GridPane;
import javafx.event.ActionEvent;
import javafx.scene.control.Alert;


public class CalculetteV1 extends Application
{
    private TextField texteFieldNombre1;
    private TextField texteFieldNombre2;
    private Button boutonAddition;
    private Button boutonSoustraction;
    private Label labelResultat;

    public static void main(String [] args)
    {
        launch(args);
    }

    public Scene calculette()
    {
        texteFieldNombre1 = new TextField();
        texteFieldNombre2 = new TextField();
        boutonAddition = new Button("+");
        boutonSoustraction = new Button("-");
        labelResultat = new Label("");
        labelResultat.setStyle("-fx-alignment: center;");

        GridPane pane = creeGridPane();

        gereeAttributsCalculette();
        gereeActionButton();

        return new Scene(pane, Donnee.largeur, Donnee.hauteur);
    }

    public GridPane creeGridPane()
    {
        GridPane gridPane = new GridPane();
        gridPane.setStyle("-fx-alignment: center;");

        gridPane.setHgap(10);
        gridPane.setVgap(10);

        gridPane.add(texteFieldNombre1, 0, 0);
        gridPane.add(texteFieldNombre2, 1, 0);
        gridPane.add(boutonAddition, 0, 1);
        gridPane.add(boutonSoustraction, 1, 1);
        gridPane.add(labelResultat, 0, 4, 2, 1);
        return gridPane;
    }

    private void gereeAttributsCalculette() {
        texteFieldNombre1.setPrefWidth(70);
        texteFieldNombre2.setPrefWidth(70);
        boutonAddition.setPrefWidth(70);
        boutonSoustraction.setPrefWidth(70);
        labelResultat.setPrefWidth(150);
    }

    public void gereeActionButton() {
        boutonAddition.setOnAction(e -> buttonEvent(e));
        boutonSoustraction.setOnAction(e -> buttonEvent(e));
    }

    public void buttonEvent(ActionEvent e)
    {
        double nombre1;
        double nombre2;
        double res;
        try
        {
            nombre1 = Float.parseFloat(texteFieldNombre1.getText());
            nombre2 = Float.parseFloat(texteFieldNombre2.getText());
            if (e.getSource() == boutonAddition)
            {
                res = nombre1 + nombre2;
            }
            else
            {
                res = nombre1 - nombre2;
            }
            labelResultat.setText("Resultat : "+res);
        }
        catch(NumberFormatException ex)
        {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("ERREUR !!!");
            alert.setHeaderText("Calcul impossible");
            alert.setContentText("Le format d'un des deux nombres est inconnu");
            alert.showAndWait();
            // labelResultat.requestFocus(); TODO
        }
    }

    @Override
    public void start(Stage primaryStage)
    {
        primaryStage.setTitle("Calculette");
        primaryStage.setScene(calculette());
        primaryStage.show();
    }
}