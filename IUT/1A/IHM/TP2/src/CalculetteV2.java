import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.control.*;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.GridPane;

public class CalculetteV2 extends Application
{
    private TextField texteFieldNombre1;
    private TextField texteFieldNombre2;
    private Button boutonOperation;
    private Label labelResultat;
    private TitledPane titre;
    private ToggleGroup groupe;

    public Button getButton()
    {
        return this.boutonOperation;
    }

    public Label getResultat()
    {
        return labelResultat;
    }

    public String getNombre1()
    {
        return texteFieldNombre1.getText();
    }

    public String getNombre2()
    {
        return texteFieldNombre2.getText();
    }

    public static void main(String [] args)
    {
        launch(args);
    }

    public Scene calculette()
    {
        texteFieldNombre1 = new TextField();
        texteFieldNombre2 = new TextField();
        boutonOperation = new Button("+");
        labelResultat = new Label("");
        labelResultat.setStyle("-fx-alignment: center;");

        boutonOperation.setOnAction(new ActionButton(this));
        boutonOperation.setAlignment(Pos.CENTER);

        GridPane pane = creeGridPane();

        gereeAttributsCalculette();

        return new Scene(pane, Donnee.largeur, Donnee.hauteur);
    }

    public GridPane creeGridPane()
    {
        GridPane gridPane = new GridPane();
        gridPane.setAlignment(Pos.CENTER);

        VBox box = creeVbox();

        gridPane.setHgap(10);
        gridPane.setVgap(10);

        gridPane.add(texteFieldNombre1, 0, 0);
        gridPane.add(texteFieldNombre2, 1, 0);
        gridPane.add(titre, 0, 1);
        gridPane.add(box, 0, 2);
        gridPane.add(boutonOperation, 0, 3);
        gridPane.add(labelResultat, 0, 4, 4, 3);
//        gridPane.setGridLinesVisible(true);
        return gridPane;
    }

    public VBox creeVbox()
    {
        ActionRadioButton act = new ActionRadioButton(this);
        RadioButton addition = new RadioButton("addition");
        RadioButton soustraction = new RadioButton("soustraction");
        RadioButton multiplication = new RadioButton("multiplication");
        RadioButton division = new RadioButton("division");
        addition.setOnAction(act);
        soustraction.setOnAction(act);
        multiplication.setOnAction(act);
        division.setOnAction(act);
        addition.setSelected(true);
        this.groupe = new ToggleGroup();
        addition.setToggleGroup(groupe);
        soustraction.setToggleGroup(groupe);
        multiplication.setToggleGroup(groupe);
        division.setToggleGroup(groupe);
        this.titre = new TitledPane();
        titre.setText("Opération");
        VBox box = new VBox();
        box.getChildren().addAll(addition,soustraction,multiplication,division);
        titre.setContent(box);
        return box;
    }

    private void gereeAttributsCalculette() {
        texteFieldNombre1.setPrefWidth(70);
        texteFieldNombre2.setPrefWidth(70);
        boutonOperation.setPrefWidth(70);
        labelResultat.setPrefWidth(150);
    }

    @Override
    public void start(Stage primaryStage)
    {
        primaryStage.setTitle("Calculette");
        primaryStage.setScene(calculette());
        primaryStage.show();
    }
}
