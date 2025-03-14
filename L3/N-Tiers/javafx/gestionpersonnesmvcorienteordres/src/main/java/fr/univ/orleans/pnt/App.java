package fr.univ.orleans.pnt;

import fr.univ.orleans.pnt.controleur.Controleur;
import fr.univ.orleans.pnt.vues.GestionnaireVue;
import fr.univ.orleans.pnt.vues.GestionnaireVueImpl;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

/**
 * JavaFX App
 */
public class App extends Application {


    @Override
    public void start(Stage stage) throws IOException {
        GestionnaireVue gestionnaireVue = new GestionnaireVueImpl(stage);
        Controleur controleur = new Controleur(gestionnaireVue);
        controleur.run();

    }


    public static void main(String[] args) {
        launch();
    }

}