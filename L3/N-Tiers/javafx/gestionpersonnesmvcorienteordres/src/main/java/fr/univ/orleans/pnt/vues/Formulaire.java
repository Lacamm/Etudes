package fr.univ.orleans.pnt.vues;

import fr.univ.orleans.pnt.controleur.Controleur;
import fr.univ.orleans.pnt.controleur.ordres.EcouteurOrdre;
import fr.univ.orleans.pnt.controleur.ordres.LanceurOrdre;
import fr.univ.orleans.pnt.controleur.ordres.TypeOrdre;
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

public class Formulaire implements VueInteractive, EcouteurOrdre {

    public static Formulaire creer(GestionnaireVue gestionnaireVue) {

        FXMLLoader fxmlLoader = new FXMLLoader(Formulaire.class.
                getResource("formulaire.fxml"));
        try {
            fxmlLoader.load();
        } catch (IOException e) {
            throw new RuntimeException("Probleme de construction de vue Formulaire");
        }
        Formulaire vue = fxmlLoader.getController();
        gestionnaireVue.ajouterEcouteurOrdre(vue);
        gestionnaireVue.ajouterVueInteractive(vue);
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

    public void enregistrerPersonne(ActionEvent actionEvent) {

        this.controleur.enregistrerPersonne(nom.getText(),prenom.getText(),
                anneeNaissance.getText(),
                email.getText(),telephone.getText());

    }

    public void afficherConfirmation(String message) {

        Alert alert = new Alert(Alert.AlertType.CONFIRMATION,"Enregistrement réussi", ButtonType.OK);
        alert.setContentText(message);
        alert.showAndWait();

    }

    public void afficherErreur(String titre, String contenu) {
        Alert alert = new Alert(Alert.AlertType.ERROR,titre, ButtonType.OK);
        alert.setContentText(contenu);
        alert.showAndWait();
    }

    @Override
    public void setAbonnement(LanceurOrdre g) {
        g.abonnement(this,
                TypeOrdre.ERREUR_NUMERO_TELEPHONE_PORTABLE,
                TypeOrdre.ERREUR_ENTIER_ATTENDU,
                TypeOrdre.ERREUR_ANNEE_SUPERIEURE_ANNEE_COURANTE,
                TypeOrdre.ERREUR_ANNEE_SUPERIEURE_1900_ATTENDUE,
                TypeOrdre.ERREUR_DONNEE_INCORRECTE,
                TypeOrdre.ERREUR_EMAIL_INCORRECT,
                TypeOrdre.DATA_NOUVELLE_PERSONNE_ENREGISTREE);
    }

    @Override
    public void traiter(TypeOrdre e) {
        switch (e) {
            case ERREUR_ENTIER_ATTENDU:{
                this.afficherErreur("Le champ année","Un entier est attendu !");
                break;
            }

            case ERREUR_EMAIL_INCORRECT: {
                this.afficherErreur("Le champ email","On attend une adresse mail bien formée");
                break;
            }

            case ERREUR_ANNEE_SUPERIEURE_1900_ATTENDUE: {
                this.afficherErreur("Le champ année","L'année de naissance doit être >= 1900");
                break;
            }


            case ERREUR_ANNEE_SUPERIEURE_ANNEE_COURANTE:{
                this.afficherErreur("Le champ année","On ne peut pas être né dans le futur !");
                break;
            }

            case ERREUR_DONNEE_INCORRECTE:{
                this.afficherErreur("Tous les champs","Tous les champs sont obligatoires !");
                break;
            }

            case ERREUR_NUMERO_TELEPHONE_PORTABLE:{
                this.afficherErreur("Le champ téléphone","On attend un numéro commençant par 06 ou 07");
                break;
            }

            case DATA_NOUVELLE_PERSONNE_ENREGISTREE:{
                this.afficherConfirmation("La personne "+nom.getText() + " "+prenom.getText()+ " a bien été enregistrée");
                break;
            }

        }

    }
}
