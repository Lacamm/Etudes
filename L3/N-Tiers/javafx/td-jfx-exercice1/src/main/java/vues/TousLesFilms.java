package vues;

import controleur.Controleur;
import controleur.ordres.EcouteurOrdre;
import controleur.ordres.LanceurOrdre;
import controleur.ordres.TypeOrdre;
import javafx.collections.FXCollections;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.control.ListCell;
import javafx.scene.control.ListView;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;
import modeleCreaFilm.Film;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;

public class TousLesFilms implements VueInteractive, EcouteurOrdre {

    @FXML
    private AnchorPane TousLesFilmsAnchorPane;
    private Controleur controleur;
    private Stage stage;
    private Scene scene;

    @FXML
    private ListView<Film> liste;;

//    public static TousLesFilms creerVue(Controleur controleur, Stage stage) throws IOException {
//        FXMLLoader fxmlLoader = new FXMLLoader(TousLesFilms.class.
//                getResource("TousLesFilms.fxml"));
//        fxmlLoader.load();
//
//        TousLesFilms vue = fxmlLoader.getController();
//        vue.initialiseScene();
//
//        vue.setControleur(controleur);
//        vue.setStage(stage);
//        return vue;
//    }

    public static TousLesFilms creer(GestionnaireVueImpl gestionnaireVue) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(Ajout.class.
                getResource("TousLesFilms.fxml"));
        fxmlLoader.load();
        TousLesFilms vue = fxmlLoader.getController();
        vue.initialiseScene();
        gestionnaireVue.ajouterVueInteractive(vue);
        gestionnaireVue.ajouterEcouteurOrdre(vue);
        return vue;
    }

    public void initialiseScene() {
        this.scene = new Scene(this.TousLesFilmsAnchorPane,640,480);
    }

    public void gotomenu(ActionEvent actionEvent) {this.getControleur().gotomenu();}

    public void initFilms(){
        Collection<Film> films = controleur.getLesFilms();
        this.liste.setItems(FXCollections.observableList(new ArrayList<>(films)));
        this.liste.setCellFactory(param -> new ListCell<Film>() {
            @Override
            protected void updateItem(Film item, boolean empty) {
                super.updateItem(item, empty);
                if (empty || item == null ) {
                    setText("");
                } else {
                    setText(item.getTitre() + " ("+item.getRealisateur()+", "+item.getGenre()+")");
                }
            }
        });
    }

    @Override
    public void setControleur(Controleur controleur) {this.controleur = controleur;}
    @Override
    public Controleur getControleur() {return controleur;}
    public Scene getScene() {
        return this.scene;
    }

    @Override
    public void setAbonnement(LanceurOrdre g) {
        g.abonnement(this, TypeOrdre.CHARGEMENT_FILM);
    }

    @Override
    public void traiter(TypeOrdre e) {
        switch (e) {
            case CHARGEMENT_FILM:
                initFilms();
        }
    }
}
