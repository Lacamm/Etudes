package fr.univ.orleans.pnt.vues;

import fr.univ.orleans.pnt.controleur.Controleur;
import fr.univ.orleans.pnt.controleur.ordres.EcouteurOrdre;
import fr.univ.orleans.pnt.controleur.ordres.LanceurOrdre;
import fr.univ.orleans.pnt.controleur.ordres.TypeOrdre;
import fr.univ.orleans.pnt.modele.Personne;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.ButtonType;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.stage.Stage;

import java.io.IOException;

public class DetailPersonne implements VueInteractive, EcouteurOrdre {

    public static DetailPersonne creer(GestionnaireVue gestionnaireVue) {

        FXMLLoader fxmlLoader = new FXMLLoader(DetailPersonne.class.
                getResource("detailpersonne.fxml"));
        try {
            fxmlLoader.load();
        } catch (IOException e) {
            throw new RuntimeException("Probleme de construction de vue Formulaire");
        }
        DetailPersonne vue = fxmlLoader.getController();
        gestionnaireVue.ajouterVueInteractive(vue);
        gestionnaireVue.ajouterEcouteurOrdre(vue);
        vue.setScene(new Scene(vue.getTop()));
        return vue;
    }

    @FXML
    private BorderPane borderPane;

    @FXML
    TextField nom;

    @FXML
    TextField prenom;

    @FXML
    TextField anneeNaissance;

    @FXML
    TextField email;

    @FXML
    TextField telephone;




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



    public void gotoAccueil(ActionEvent actionEvent) {
        this.getControleur().gotoMenu();
    }


    @Override
    public void setAbonnement(LanceurOrdre g) {
        g.abonnement(this,TypeOrdre.DATA_PERSONNE_SELECTIONNEE);
    }

    @Override
    public void traiter(TypeOrdre e) {
        switch (e) {
            case DATA_PERSONNE_SELECTIONNEE: {
                Personne personne = this.getControleur().getPersonneSelectionnee();
                this.nom.setText(personne.getNom());
                this.prenom.setText(personne.getPrenom());
                this.email.setText(personne.getEmail());
                this.telephone.setText(personne.getNumeroPortable());
                this.anneeNaissance.setText(String.valueOf(personne.getAnneeNaissance()));
                break;
            }
        }
    }
}
