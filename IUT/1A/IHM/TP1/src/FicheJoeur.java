import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.TextField;
import javafx.scene.control.Label;
import javafx.geometry.Insets;
import javafx.scene.control.Button;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.scene.control.TitledPane;
import javafx.scene.control.ToggleGroup;
import javafx.scene.control.RadioButton;
import javafx.scene.control.ComboBox;
import javafx.collections.ObservableList;
import javafx.collections.FXCollections;
import javafx.scene.image.ImageView;
import javafx.scene.text.Font;


public class FicheJoeur extends Application
{
    public static void main(String [] args)
    {
        launch(args);
    }

    public Scene creeFicheJoueur()
    {
        Label lNom = new Label("Fiche Joueur");
        lNom.setStyle("-fx-alignment: center; -fx-background-color: white;");
        lNom.setMaxSize(Double.MAX_VALUE, Double.MAX_VALUE);
        lNom.setFont(new Font(25));

        BorderPane panel = new BorderPane();

        panel.setTop(lNom);
        panel.setCenter(creePaneCentral());
        panel.setLeft(creePaneGauche());
        panel.setBottom(creePaneBas());

        int largeurPanel = 500;
        int hauteurPanel = 400;
        return new Scene(panel, largeurPanel, hauteurPanel);
    }

    public VBox creePaneGauche()
    {


        VBox box = new VBox();
//        box.setPrefWidth(100);
        double boutonsize = 100;
        Button deb = new Button("Debut");
        deb.setPrefWidth(boutonsize);
        Button prec = new Button("Prec");
        prec.setPrefWidth(boutonsize);
        Button valider = new Button("Valider");
        valider.setPrefWidth(boutonsize);
        Button nouv = new Button("Nouveau");
        nouv.setPrefWidth(boutonsize);
        Button suiv = new Button("Suiv");
        suiv.setPrefWidth(boutonsize);
        Button dern = new Button("Dern");
        dern.setPrefWidth(boutonsize);

        box.getChildren().add(deb);
        box.getChildren().add(prec);
        box.getChildren().add(valider);
        box.getChildren().add(nouv);
        box.getChildren().add(suiv);
        box.getChildren().add(dern);

//        box.set(4);
        box.setStyle("-fx-alignment: center; -fx-background-color: mistyrose;");

        return box;

    }

    public BorderPane creePaneBas()
    {
        Label lNombre = new Label("Nb de fichies: 102");
        Label lNumero = new Label("Numero de la fiche: 10");
        Label lFiche = new Label("Fiche Modifie");

        BorderPane Bpane = new BorderPane();
        Bpane.setLeft(lNombre);
        Bpane.setCenter(lNumero);
        Bpane.setRight(lFiche);
        Bpane.setStyle("-fx-alignment: center; -fx-background-color: aquamarine;");

        return Bpane;
    }

    public GridPane creePaneCentral()
    {
        Label lPseudo = new Label("Pseudo : ");
        TextField tPseudo = new TextField();

        Label lMDP = new Label("Mot de passe : ");
        TextField tMDP = new TextField();

        Label lNiveau = new Label("Niveau : ");
        ObservableList<String> ObsvervableNiveau=FXCollections.observableArrayList("1","2", "3");
        ComboBox<String> listeNiveau = new ComboBox<>(ObsvervableNiveau);

        RadioButton masc = new RadioButton("Homme");
        RadioButton fem = new RadioButton("Femme");
        ToggleGroup groupe = new ToggleGroup();
        masc.setToggleGroup(groupe);
        fem.setToggleGroup(groupe);
        TitledPane titre = new TitledPane();
        titre.setText("Sexe");
        VBox box = new VBox();
        box.getChildren().addAll(masc,fem);
        titre.setContent(box);

        ImageView img = new ImageView("./img/Kali.jpg");
        img.setFitWidth(100);
        img.setPreserveRatio(true);

        GridPane grid = new GridPane();

        grid.add(img, 4, 1);
        grid.add(lPseudo, 2, 2);
        grid.add(tPseudo, 3, 2);
        grid.add(lMDP, 2, 3);
        grid.add(tMDP, 3, 3);
        grid.add(lNiveau, 2, 4);
        grid.add(listeNiveau, 3, 4);
        grid.add(titre, 3, 5);
        grid.add(box, 3, 5);
        grid.setVgap(4);
//        grid.setGridLinesVisible(true);
        grid.setStyle("-fx-background-color: lightseagreen;");
        return grid;
    }

    @Override
    public void start(Stage primaryStage)
    {
        primaryStage.setTitle("TP1 Formulaire complet");
        primaryStage.setScene(creeFicheJoueur());
        primaryStage.show();
    }
}