package vues;

import controleur.ordres.LanceurOrdre;
import controleur.ordres.TypeOrdre;

import javafx.stage.Stage;

import java.io.IOException;

public class GestionnaireVueImpl extends GestionnaireVue {
    private Menu menu;
    private Ajout ajout;
    private TousLesFilms touslesfilms;


    public GestionnaireVueImpl(Stage stage) throws IOException {
        super(stage);
        this.menu = Menu.creer(this);
        this.ajout = Ajout.creer(this);
        this.touslesfilms = TousLesFilms.creer(this);
    }

    @Override
    public void setAbonnement(LanceurOrdre lanceur) {
        super.setAbonnement(lanceur);
        lanceur.abonnement(this,
                TypeOrdre.SHOW_MENU,
                TypeOrdre.SHOW_AJOUT,
                TypeOrdre.SHOW_TOUSLESFILMS);

    }

    @Override
    public void traiter(TypeOrdre ordre) {
        switch (ordre) {
            case SHOW_MENU:{
                this.getStage().setScene(menu.getScene());
                break;
            }

            case SHOW_AJOUT: {
                this.getStage().setScene(ajout.getScene());
                break;
            }

            case SHOW_TOUSLESFILMS: {
                this.getStage().setScene(touslesfilms.getScene());
                break;
            }
            case DO_VIDER_CHAMPS: {
                this.ajout.viderChamps();
                break;
            }
            case CHARGEMENT_GENRE: {
                this.ajout.chargerGenres();
            }
            case CHARGEMENT_FILM: {
                this.touslesfilms.initFilms();
            }
        }
        this.getStage().show();
    }
}
