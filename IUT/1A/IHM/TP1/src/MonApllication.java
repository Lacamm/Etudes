import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.FlowPane;
import javafx.scene.control.TextField;
import javafx.scene.control.Label;
import javafx.geometry.Insets;
import javafx.scene.control.Button;
import javafx.scene.layout.GridPane;

public class MonApllication extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    public Scene creeFormulaire()
    {
        Label lNom = new Label("Nom :");
        TextField tNom = new TextField();

        Label lPrenom = new Label("Prenom :");
        TextField tPrenom = new TextField();

        Label lMDP = new Label("Choisissez un mot de passe :");
        TextField tMDP = new TextField();

        Button Valider = new Button("Valider");

        FlowPane panel = new FlowPane();
        panel.getChildren().add(lNom);
        panel.getChildren().add(tNom);
        panel.getChildren().add(lPrenom);
        panel.getChildren().add(tPrenom);
        panel.getChildren().add(lMDP);
        panel.getChildren().add(tMDP);
        panel.getChildren().add(Valider);
        panel.setVgap(5);
        panel.setHgap(10);
        panel.setPadding(new Insets(10, 10, 10, 3));

        int largeurPanel = 500;
        int hauteurPanel = 100;
        return new Scene(panel, largeurPanel, hauteurPanel);
    }

    public Scene creeFormulaireGrid()
    {
        Label lNom = new Label("Nom :");
        TextField tNom = new TextField();

        Label lPrenom = new Label("Prenom :");
        TextField tPrenom = new TextField();

        Label lMDP = new Label("Choisissez un mot de passe :");
        TextField tMDP = new TextField();

        Button Valider = new Button("Valider");

        GridPane grid = new GridPane();
        grid.add(lNom, 2, 1);
        grid.add(tNom, 3, 1);
        grid.add(lPrenom, 2, 2);
        grid.add(tPrenom, 3, 2);
        grid.add(lMDP, 2, 3);
        grid.add(tMDP, 3, 3);
        grid.add(Valider, 3, 4);
        // grid.setGridLinesVisible(true);

        int largeurPanel = 500;
        int hauteurPanel = 100;
        return new Scene(grid, largeurPanel, hauteurPanel);
    }

    @Override
    public void start(Stage primaryStage)
    {
        primaryStage.setTitle("Ma  premiere  application  JavaFX");
        primaryStage.setScene(creeFormulaire());
        // primaryStage.setScene(creeFormulaireGrid());
        primaryStage.show();
    }
}