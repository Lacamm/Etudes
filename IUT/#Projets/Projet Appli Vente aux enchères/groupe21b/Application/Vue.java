import javafx.application.*;
import javafx.geometry.*;
import javafx.scene.*;
import javafx.stage.*;
import javafx.scene.control.*;
import javafx.scene.image.*;
import javafx.scene.layout.*;
import javafx.scene.paint.*;
import javafx.scene.text.*;
import java.util.*;
import java.io.*;

public class Vue extends Application {

    private List<Image> lesImages;

    public static void main(String[] args) {
        launch(args);
    }

    @Override
	public void start(Stage stage) {
        this.chargerImages("./img");
	    stage.setTitle("Application de vente aux enchères");
	    stage.setScene(this.accueil());
	    stage.show();
	}

    private void chargerImages(String repertoire) {
		this.lesImages = new ArrayList<Image>();
		for (int i = 0; i < 1; i++) {
		    File file = new File(repertoire + "/vae" + i + ".png");
		    System.out.println(file.toURI().toString());
			this.lesImages.add(new Image(file.toURI().toString()));
		}
	}


    public Scene accueil() {

        // Haut
        Label titre = new Label("Accueil");
        titre.setFont(Font.font(40));

        // Centre
        VBox vb = new VBox(5);
        ImageView dessin = new ImageView(this.lesImages.get(0));
        Label desc = new Label("Bienvenue sur l'application de vente aux enchères");
        Button connexion = new Button("Se connecter");
        Button inscription = new Button("S'inscrire");

        vb.setAlignment(Pos.CENTER);
        dessin.setFitWidth(200);
        dessin.setPreserveRatio(true);
        desc.setFont(Font.font(25));

        // Boutons
        HBox hb = new HBox(5);
        connexion.setMinSize(120, 20);
        inscription.setMinSize(120, 20);
        connexion.setOnAction(new ActionConnexion(this));
        inscription.setOnAction(new ActionInscription(this));
        hb.getChildren().addAll(connexion, inscription);
        hb.setPadding(new Insets(5, 5, 5, 5));
        hb.setAlignment(Pos.CENTER);
        hb.setSpacing(20);

        vb.getChildren().addAll(dessin, desc, hb);
        vb.setAlignment(Pos.CENTER);

        // Panel principal
        BorderPane bp = new BorderPane();
        bp.setTop(titre);
        bp.setCenter(vb);
        
        return new Scene(bp, 800, 800);
    }
    
}