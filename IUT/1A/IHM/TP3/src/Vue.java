import javafx.application.Application;
import javafx.stage.Stage;

public class Vue extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Meilleures Scores");
        primaryStage.setScene(creeFormulaire());
        primaryStage.show();
    }

    public Scene creeFormulaire(){

        return new Scene();
    }
}
