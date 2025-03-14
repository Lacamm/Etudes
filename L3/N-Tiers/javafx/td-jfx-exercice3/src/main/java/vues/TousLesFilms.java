package vues;

import controleur.Controleur;
import javafx.collections.FXCollections;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.ListCell;
import javafx.scene.control.ListView;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import modeleCreaFilm.Film;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;

public class TousLesFilms extends Vue implements VueInteractive {
    private Controleur controleur;

    @FXML
    VBox mainVbox;

    @FXML
    ListView<Film> lesFilms;

    public Parent getTop() {
        return mainVbox;
    }

    public static TousLesFilms creerVue(Controleur controleur, Stage stage) {
        FXMLLoader fxmlLoader = new FXMLLoader(TousLesFilms.class.getResource("tousLesFilms.fxml"));
        try {
            fxmlLoader.load();
        } catch (IOException e) {
            System.out.println("Probleme de construction de vue Formulaire");
        }
        TousLesFilms vue = fxmlLoader.getController();

        vue.setControleur(controleur);
        vue.setStage(stage);
        vue.setScene(new Scene(vue.getTop()));
        return vue;

    }
    public void gotomenu(ActionEvent actionEvent) {
        controleur.gotoMenu();
    }


    @Override
    public void setControleur(Controleur controleur) {
        this.controleur = controleur;
    }



    @Override
    public void show() {
        Collection<Film> films = controleur.getLesFilms();
        this.lesFilms.setItems(FXCollections.observableList(new ArrayList<>(films)));
        this.lesFilms.setCellFactory(param -> new ListCell<Film>() {
            @Override
            protected void updateItem(Film item, boolean empty) {
                super.updateItem(item, empty);
                if (empty || item == null ) {
                    setText("No body");
                } else {
                    setText(item.getTitre() + " ("+item.getRealisateur()+", "+item.getGenre()+")");
                }
            }
        });
        super.show();
    }
}
