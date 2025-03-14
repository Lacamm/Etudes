import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.*;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.stage.Stage;


public class MonApplication extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    public Scene creerFormulaire(){
        FlowPane panel = new FlowPane();

        // création nom
        Label lNom=new Label("Nom :");
        TextField tNom = new TextField();

        // création prenom
        Label lprenom=new Label("Prenom :");
        TextField tprenom = new TextField();

        // création mdp
        Label lmdp=new Label("Mot de passe :");
        PasswordField tmdp = new PasswordField();

        // création bouton
        Button tbouton = new Button("Valider");

        panel.getChildren().addAll(lNom,tNom,lprenom,tprenom,lmdp,tmdp,tbouton);

        panel.setVgap(2);
        panel.setHgap(2);
        panel.setPadding(new Insets(5,2,5,2));

        return new Scene(panel ,500 ,100);
    }

    public Scene creerFormulaireGrid() {
        // création nom
        Label lNom = new Label("Nom :");
        TextField tNom = new TextField();

        // création prenom
        Label lprenom = new Label("Prenom :");
        TextField tprenom = new TextField();

        // création mdp
        Label lmdp = new Label("Mot de passe :");
        PasswordField tmdp = new PasswordField();

        // création bouton
        Button tbouton = new Button("Valider");

        //création grid

        GridPane p = new GridPane();
        p.add(lNom, 1, 1);
        p.add(tNom, 2, 1);
        p.add(lprenom, 1, 2);
        p.add(tprenom, 2, 2);
        p.add(lmdp, 1, 3);
        p.add(tmdp, 2, 3);
        p.add(tbouton, 2, 4);

        p.setVgap(5);

        return new Scene(p, 500, 500);
    }



    public Scene creerFormumlairePingouin(){
        BorderPane b = new BorderPane();
        b.setLeft(creerGauche());
        b.setTop(creerHaut());
        b.setRight(creerDroite());
        b.setBottom(creerBas());
        b.setCenter(creerCentre());

        return new Scene(b,500,500);
    }

    public BorderPane creerBas(){
        BorderPane b = new BorderPane();
        Label nb = new Label("Nb de fiches: 102");
        Label num = new Label("Numéro de la fiche: 10");
        Label modif = new Label("Fiche modifiée");

        b.setLeft(nb);
        b.setCenter(num);
        b.setRight(modif);

        return b;
    }

    public VBox creerGauche() {
        // création bouton
        Button debut = new Button("Début");
        debut.setPrefWidth(85);
        Button prec = new Button("Prec");
        prec.setPrefWidth(85);
        Button valider = new Button("Valider");
        valider.setPrefWidth(85);
        Button nouveau = new Button("Nouveau");
        nouveau.setPrefWidth(85);
        Button suiv = new Button("Suiv");
        suiv.setPrefWidth(85);
        Button dern = new Button("Dern");
        dern.setPrefWidth(85);

        // ajout des boutuons à la Vbox

        VBox v = new VBox();
        v.getChildren().addAll(debut,prec,valider,nouveau,suiv,dern);
        v.setPrefSize(100,500);
        v.setSpacing(3);
        v.setStyle("-fx-alignment: center; -fx-background-color: lightpink;");

        return v;
    }

    public TextField creerHaut(){
        TextField titre = new TextField("Fiche Joueur");
        titre.setFont(Font.font(24));
        titre.setStyle("-fx-alignment: center; -fx-background-color: gainsboro;");

        return titre;
    }

    public GridPane creerCentre(){
        GridPane g = new GridPane();

        // création des champs
        Label lpseudo = new Label("Pseudo:");
        TextField tpseudo = new TextField();
        Label lmdp = new Label("Mot de passe:");
        PasswordField tmdp = new PasswordField();

        g.add(lpseudo,2,2);
        g.add(tpseudo,3,2);

        g.add(lmdp,2,3);
        g.add(tmdp,3,3);

        Label lNiveau = new Label("Niveau : ");
        ObservableList<String> ObsvervableNiveau= FXCollections.observableArrayList("1","2", "3");
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

        g.setStyle("-fx-alignment: center;-fx-background-color: teal;");

        return g;
    }

    public VBox creerDroite(){
        ImageView img = new ImageView("/pingouin.png");
        img.setFitWidth (100);
        img.setPreserveRatio(true);

        VBox v = new VBox();
        v.setStyle("-fx-background-color: teal;");
        v.getChildren().addAll(img);
        return v;
    }

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Ma première appli");
        primaryStage.setScene(creerFormumlairePingouin());
        primaryStage.show();
    }
}
