package fr.univ.orleans.pnt.controleur;

import fr.univ.orleans.pnt.controleur.ordres.EcouteurOrdre;
import fr.univ.orleans.pnt.controleur.ordres.LanceurOrdre;
import fr.univ.orleans.pnt.controleur.ordres.TypeOrdre;
import fr.univ.orleans.pnt.modele.FacadeGestionPersonnes;
import fr.univ.orleans.pnt.modele.Personne;
import fr.univ.orleans.pnt.modele.exceptions.*;
import fr.univ.orleans.pnt.vues.*;
import javafx.stage.Stage;

import java.util.*;

public class Controleur implements LanceurOrdre {

    private FacadeGestionPersonnes facadeGestionPersonnes;
    private Map<TypeOrdre,Collection<EcouteurOrdre>> abonnes;



    public Controleur(GestionnaireVue gestionnaireVue) {

        this.abonnes = new HashMap<>();
        Arrays.stream(TypeOrdre.values())
                .forEach(
                        typeOrdre ->
                                this.abonnes.put(typeOrdre,new ArrayList<>()));

        this.facadeGestionPersonnes = new FacadeGestionPersonnes();
        gestionnaireVue.setControleur(this);
        gestionnaireVue.setAbonnement(this);


    }

    public void run() {
        this.fireOrdre(TypeOrdre.SHOW_ACCUEIL);

    }


    public void gotoFormulaire() {
        this.fireOrdre(TypeOrdre.SHOW_FORMULAIRE);
    }

    public void gotoPersonnes() {
        this.fireOrdre(TypeOrdre.SHOW_PERSONNES);

    }

    public void gotoMenu() {

        this.fireOrdre(TypeOrdre.SHOW_ACCUEIL);
    }

    public void enregistrerPersonne(String nomText, String prenomText,
                                    String anneeNaissanceText,
                                    String emailText,
                                    String telephoneText) {
        try {
            this.facadeGestionPersonnes.enregistrerPersonne(nomText, prenomText, anneeNaissanceText, emailText, telephoneText);
            this.fireOrdre(TypeOrdre.DATA_NOUVELLE_PERSONNE_ENREGISTREE);
            this.gotoPersonnes();


        } catch (DonneeIncorrecteException e) {
            this.fireOrdre(TypeOrdre.ERREUR_DONNEE_INCORRECTE);
        } catch (EntierAttenduException e) {
            this.fireOrdre(TypeOrdre.ERREUR_ENTIER_ATTENDU);

        } catch (AnneeSuperieure1900AttendueException e) {
            this.fireOrdre(TypeOrdre.ERREUR_ANNEE_SUPERIEURE_1900_ATTENDUE);
        } catch (AnneeSuperieureAnneeCouranteException e) {
            this.fireOrdre(TypeOrdre.ERREUR_ANNEE_SUPERIEURE_ANNEE_COURANTE);
        } catch (EmailIncorrectException e) {
            this.fireOrdre(TypeOrdre.ERREUR_EMAIL_INCORRECT);
        } catch (NumeroTelephonePortableIncorrectException e) {
            this.fireOrdre(TypeOrdre.ERREUR_NUMERO_TELEPHONE_PORTABLE);
        }

    }

    public Collection<Personne> getPersonnes() {

        return this.facadeGestionPersonnes.getPersonnes();
    }

    private Personne personneSelectionnee;

    public Personne getPersonneSelectionnee() {
        return personneSelectionnee;
    }

    public void setPersonneSelectionnee(Personne personneSelectionnee) {
        this.personneSelectionnee = personneSelectionnee;
        this.fireOrdre(TypeOrdre.DATA_PERSONNE_SELECTIONNEE);
        this.fireOrdre(TypeOrdre.SHOW_DETAIL_PERSONNE);
    }

    @Override
    public void abonnement(EcouteurOrdre ecouteurOrdre, TypeOrdre... types) {
/*
        for (TypeOrdre typeOrdre : types){
            this.abonnes.get(typeOrdre).add(ecouteurOrdre);
        }
        Equivalent à ce qu'il y a ci-dessous
*/
        Arrays.stream(types).forEach(typeOrdre ->
        {this.abonnes.get(typeOrdre).add(ecouteurOrdre);});

    }

    @Override
    public void fireOrdre(TypeOrdre e) {
            this.abonnes.get(e)
                    .stream()
                    .forEach(abonne ->
                            abonne.traiter(e));
    }
}
