package fr.univ.orleans.pnt.vues;

import fr.univ.orleans.pnt.controleur.Controleur;
import fr.univ.orleans.pnt.controleur.ordres.EcouteurOrdre;
import fr.univ.orleans.pnt.controleur.ordres.LanceurOrdre;
import fr.univ.orleans.pnt.controleur.ordres.TypeOrdre;
import fr.univ.orleans.pnt.modele.Personne;
import javafx.collections.FXCollections;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.ListCell;
import javafx.scene.control.ListView;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

import java.io.IOException;
import java.util.Collection;
import java.util.Objects;

public class Personnes implements VueInteractive, EcouteurOrdre {

    public static Personnes creer(GestionnaireVue gestionnaireVue) {

        FXMLLoader fxmlLoader = new FXMLLoader(Personnes.class.
                getResource("personnes.fxml"));
        try {
            fxmlLoader.load();
        } catch (IOException e) {
            throw new RuntimeException("Probleme de construction de vue Personnes");
        }
        Personnes vue = fxmlLoader.getController();
        gestionnaireVue.ajouterVueInteractive(vue);
        gestionnaireVue.ajouterEcouteurOrdre(vue);
        vue.setScene(new Scene(vue.getTop()));
        vue.costumizeListView();
        return vue;
    }


    @FXML
    private BorderPane borderPane;



    @FXML
    private ListView<Personne> personnes;

    private Controleur controleur;


    private Scene scene;


    private void costumizeListView() {
        personnes.setCellFactory(param -> new ListCell<Personne>() {
            @Override
            protected void updateItem(Personne item, boolean empty) {
                super.updateItem(item, empty);
                if (empty || item == null || item.getNom() == null) {
                    setText("");
                } else {
                    setText(item.getNom()+" "+item.getPrenom());
                }
            }
        });

        personnes.setOnMouseClicked(e -> {
            if (e.getClickCount() == 2) {
                Personne personne = personnes.
                        getSelectionModel().
                        getSelectedItem();
                if (Objects.nonNull(personne)) {
                    this.controleur.setPersonneSelectionnee(personne);
                }

            }

        });




    }



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



    public void gotoMenu(ActionEvent actionEvent) {
        this.getControleur().gotoMenu();
    }

    @Override
    public void setAbonnement(LanceurOrdre g) {
        g.abonnement(this,TypeOrdre.DATA_NOUVELLE_PERSONNE_ENREGISTREE);
    }

    @Override
    public void traiter(TypeOrdre e) {
        switch (e) {
            case DATA_NOUVELLE_PERSONNE_ENREGISTREE: {
                Collection<Personne> personneCollection = this.getControleur().getPersonnes();
                personnes.setItems(FXCollections.observableArrayList(personneCollection));

                break;
            }
        }
    }
}
