package vues;

import controleur.Controleur;
import controleur.ordres.EcouteurOrdre;
import controleur.ordres.LanceurOrdre;
import controleur.ordres.TypeOrdre;
import javafx.collections.FXCollections;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.ComboBox;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import modeleCreaFilm.Film;
import modeleCreaFilm.GenreFilm;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;

public class Ajout implements VueInteractive , EcouteurOrdre {

    @FXML
    private AnchorPane AjoutAnchorPane;
    private Controleur controleur;
    private Stage stage;
    private Scene scene;

    @FXML
    TextField titre;
    @FXML
    ComboBox<GenreFilm> comboboxGenre;
    @FXML
    TextField realisateur;

    public static Ajout creer(GestionnaireVueImpl gestionnaireVue) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(Ajout.class.
                getResource("Ajout.fxml"));
        fxmlLoader.load();
        Ajout vue = fxmlLoader.getController();
        vue.initialiseScene();
        gestionnaireVue.ajouterVueInteractive(vue);
        gestionnaireVue.ajouterEcouteurOrdre(vue);
        return vue;
    }

    public void creerFilm(ActionEvent actionEvent) {
        controleur.creerFilm(titre.getText(), comboboxGenre.getValue().name(), realisateur.getText());
        this.controleur.fireOrdre(TypeOrdre.CHARGEMENT_FILM);
        viderChamps();
    }

    public  void chargerGenres(){this.comboboxGenre.setItems(FXCollections.observableList(new ArrayList<>(controleur.getGenres())));}
    public void gotomenu(ActionEvent actionEvent) {this.getControleur().gotomenu();}

    public void initialiseScene() {
        this.scene = new Scene(this.AjoutAnchorPane,640,480);
    }

    @Override
    public void setControleur(Controleur controleur) {this.controleur = controleur;}
    @Override
    public Controleur getControleur() {return controleur;}

    public Scene getScene() {return this.scene;}

    public void afficherErreur(String erreur_de_genre, String s) {}

    public void viderChamps() {
        titre.setText("");
        realisateur.setText("");
        comboboxGenre.getSelectionModel().clearSelection();
    }

    @Override
    public void setAbonnement(LanceurOrdre g) {
        g.abonnement(this, TypeOrdre.CHARGEMENT_GENRE);
    }

    @Override
    public void traiter(TypeOrdre e) {
        switch (e) {
            case CHARGEMENT_GENRE:
                this.comboboxGenre.setItems(FXCollections.observableList(new ArrayList<>(this.controleur.getGenres())));
        }
    }
}
