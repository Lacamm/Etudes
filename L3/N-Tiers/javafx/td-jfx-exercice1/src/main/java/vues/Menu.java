package vues;

import controleur.Controleur;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import javafx.scene.text.Font;
import javafx.stage.Stage;

import java.lang.ref.PhantomReference;

public class Menu implements VueInteractive {

    private static final Integer LARGEUR_FENETRE = 640;
    private static final Integer LONGUEUR_FENETRE = 480;

    private Controleur controleur;
    private Stage stage;
    private Scene scene;

    public static Menu creer(GestionnaireVueImpl gestionnaireVue) {
        Menu vue = new Menu();
        gestionnaireVue.ajouterVueInteractive(vue);
        vue.initialiserComposants();
        return vue;
    }

    public void initialiserComposants(){
        BorderPane rootElement = new BorderPane();
        VBox bouttons = new VBox();

        Label titre = new Label("Les Films");
        Button consulte = new Button("Consulter");
        Button ajout = new Button("Ajouter");

        titre.setMaxWidth(Double.MAX_VALUE);
        titre.setAlignment(Pos.CENTER);
        titre.setFont(Font.font(40));

        //consulte.setMaxWidth(Double.MAX_VALUE);
        consulte.setAlignment(Pos.CENTER);
        consulte.setFont(Font.font(25));
        consulte.addEventHandler(ActionEvent.ACTION, e-> {
            this.gotoTousLesFilms(e);}
        );

        //ajout.setMaxWidth(Double.MAX_VALUE);
        ajout.setAlignment(Pos.CENTER);
        ajout.setFont(Font.font(25));
        ajout.addEventHandler(ActionEvent.ACTION, e -> {
            this.gotoAjout(e);
        });

        bouttons.getChildren().add(consulte);
        bouttons.getChildren().add(ajout);
        bouttons.setAlignment(Pos.CENTER);
        bouttons.setSpacing(40);

        rootElement.setTop(titre);
        rootElement.setCenter(bouttons);

        scene = new Scene(rootElement, LARGEUR_FENETRE, LONGUEUR_FENETRE);
    }

    @Override
    public void setControleur(Controleur controleur) {this.controleur = controleur;}
    @Override
    public Controleur getControleur() {return controleur;}
    public Scene getScene() {return this.scene;}

    public void setStage(Stage stage) {this.stage = stage;}
    public void setScene(Scene scene) {this.scene = scene;}

    public void gotoAjout(ActionEvent actionEvent) {this.getControleur().gotoajout();}
    public void gotoTousLesFilms(ActionEvent actionEvent) {this.getControleur().gototouslesfilms();}

}
