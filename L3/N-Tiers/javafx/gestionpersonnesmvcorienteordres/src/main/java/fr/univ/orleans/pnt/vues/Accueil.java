package fr.univ.orleans.pnt.vues;

import fr.univ.orleans.pnt.controleur.Controleur;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

import java.io.IOException;

public class Accueil implements VueInteractive {

    public static Accueil creer(GestionnaireVue gestionnaireVue) {

        FXMLLoader fxmlLoader = new FXMLLoader(Accueil.class.
                getResource("accueil.fxml"));
        try {
            fxmlLoader.load();
        } catch (IOException e) {
            throw new RuntimeException("Probleme de construction de vue Accueil");
        }
        Accueil vue = fxmlLoader.getController();
        gestionnaireVue.ajouterVueInteractive(vue);
        vue.setScene(new Scene(vue.getTop()));
        return vue;
    }


    @FXML
    private BorderPane borderPane;

    private Controleur controleur;

    private Scene scene;


    public Parent getTop() {
        return borderPane;
    }



    public Scene getScene() {
        return scene;
    }

    public void setScene(Scene scene) {
        this.scene = scene;
    }

    @Override
    public void setControleur(Controleur controleur) {
        this.controleur = controleur;
    }

    @Override
    public Controleur getControleur() {
        return controleur;
    }


    public void gotoFormulaire(ActionEvent actionEvent) {
        this.getControleur().gotoFormulaire();
    }

    public void gotoPersonnes(ActionEvent actionEvent) {
        this.getControleur().gotoPersonnes();
    }
}
