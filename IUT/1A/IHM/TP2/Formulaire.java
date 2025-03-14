import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;

public class Formulaire extends Application{
    private TextField tf;

    public static void main(String[]args){
        launch(args);
    }

    String getTf(){return this.tf.getText();}
    void effaceTf(){this.tf.setText("");}


    public Scene creationScene(){
        VBox vb = new VBox(5);
        vb.setAlignment((Pos.CENTER));
        Button b1 = new Button("Boutton 1");
    }


    public Scene clic(){
        Button but = new Button("Bouton 1");
        BorderPane b = new BorderPane();
        b.setCenter(but);
        return new Scene(b,500,500);
    }

    @Override
    public void start(Stage primaryStage){
        primaryStage.setTitle("Prog evenementielle");
        primaryStage.setScene(clic());
        primaryStage.show();
    }
}
