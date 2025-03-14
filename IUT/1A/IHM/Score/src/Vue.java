import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;



public class Vue extends Application {
    private Scores scores;
    private TextField t1;
    private TextField t2;
    private ListView<String> tableau;
    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Meilleurs scores");
        primaryStage.setScene(scene());
        primaryStage.setResizable(false);
        primaryStage.show();
    }

    public Scene scene(){
        VBox box = new VBox();
        VBox vbox = new VBox();
        HBox box2 = new HBox();
        this.t1 = new TextField();
        this.t2 = new TextField();
        this.tableau = new ListView<String>();
        Label l1 = new Label("Nom du joueur:");
        Label l2 = new Label("Points obtenus:");
        Button b = new Button("Valider");
        vbox.getChildren().addAll(box2,b);
        Controleur action =new Controleur(this);
        b.setOnAction(action);
        TitledPane pane = new TitledPane();
        pane.setCollapsible(false);
        pane.setContent(this.tableau);
        pane.setText("Tableau des scores");
        box2.getChildren().addAll(l1,t1,l2,t2);
        box.getChildren().add(box2);
        box.getChildren().add(vbox);
        box.getChildren().add(pane);
        pane.setPadding(new Insets(90,120,120,120));
        box.setPadding(new Insets(10,10,10,10));
        vbox.setPadding(new Insets(50,10,10,10));
        vbox.setAlignment(Pos.CENTER);
        box2.setSpacing(10);

        return new Scene(box,600,500);
    }
     public TextField getNomJoueur(){ return this.t1;}

     public TextField getNbPoints(){ return this.t2;}

     public ListView<String> getTableau(){return this.tableau;}

}

