package fr.univ.orleans.pnt.vues;

import fr.univ.orleans.pnt.controleur.ordres.LanceurOrdre;
import fr.univ.orleans.pnt.controleur.ordres.TypeOrdre;
import javafx.stage.Stage;

public class GestionnaireVueImpl extends GestionnaireVue {
    private Accueil accueil;
    private DetailPersonne detailPersonne;
    private Personnes personnes;
    private Formulaire formulaire;


    public GestionnaireVueImpl(Stage stage) {
        super(stage);
        this.accueil = Accueil.creer(this);
        this.detailPersonne = DetailPersonne.creer(this);
        this.personnes = Personnes.creer(this);
        this.formulaire = Formulaire.creer(this);
    }

    @Override
    public void setAbonnement(LanceurOrdre g) {
        super.setAbonnement(g);
        g.abonnement(this,
                TypeOrdre.SHOW_FORMULAIRE,
                TypeOrdre.SHOW_ACCUEIL,
                TypeOrdre.SHOW_PERSONNES,
                TypeOrdre.SHOW_DETAIL_PERSONNE);

    }

    @Override
    public void traiter(TypeOrdre e) {
        switch (e) {
            case SHOW_FORMULAIRE:{
                this.getStage().setScene(formulaire.getScene());
                break;
            }

            case SHOW_ACCUEIL: {
                this.getStage().setScene(accueil.getScene());
                break;
            }

            case SHOW_DETAIL_PERSONNE: {
                this.getStage().setScene(detailPersonne.getScene());
                break;
            }

            case SHOW_PERSONNES: {
                this.getStage().setScene(personnes.getScene());
                break;
            }
        }
        this.getStage().show();

    }
}
