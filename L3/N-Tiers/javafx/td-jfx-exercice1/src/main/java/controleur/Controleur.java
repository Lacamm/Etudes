package controleur;

import facadeCreaFilm.FacadeScreen;

import facadeCreaFilm.FacadeScreenImpl;
import facadeCreaFilm.GenreNotFoundException;
import facadeCreaFilm.NomFilmDejaExistantException;
import javafx.application.Platform;
import javafx.scene.control.Alert;
import javafx.stage.Stage;
import modeleCreaFilm.Film;
import modeleCreaFilm.GenreFilm;
import vues.Ajout;
import vues.GestionnaireVue;
import vues.Menu;
import vues.TousLesFilms;
import controleur.ordres.LanceurOrdre;
import controleur.ordres.EcouteurOrdre;
import controleur.ordres.TypeOrdre;

import java.io.IOException;
import java.util.*;

public class Controleur implements LanceurOrdre{

    private FacadeScreen facadeScreen;
    private Map<TypeOrdre,Collection<EcouteurOrdre>> abonnes;

    public Controleur(GestionnaireVue gestionnaireVue) {
        this.abonnes = new HashMap<>();
        Arrays.stream(TypeOrdre.values())
                .forEach(
                        typeOrdre ->
                                this.abonnes.put(typeOrdre,new ArrayList<>()));

        this.facadeScreen = new FacadeScreenImpl();
        gestionnaireVue.setControleur(this);
        gestionnaireVue.setAbonnement(this);

        this.fireOrdre(TypeOrdre.CHARGEMENT_GENRE);
        this.fireOrdre(TypeOrdre.CHARGEMENT_FILM);
    }

    public void run() {this.fireOrdre(TypeOrdre.SHOW_MENU);}

    public void gotomenu() {this.fireOrdre(TypeOrdre.SHOW_MENU);}
    public void gotoajout() {this.fireOrdre(TypeOrdre.SHOW_AJOUT);}
    public void gototouslesfilms() {this.fireOrdre(TypeOrdre.SHOW_TOUSLESFILMS);}


    public Collection<GenreFilm> getGenres() {
        return this.facadeScreen.getAllGenres();
    }
    public Collection<Film> getLesFilms() {
        return facadeScreen.getAllFilms();
    }

    public void creerFilm(String titre, String genre, String realisateur)  {
        try {
            facadeScreen.creerFilm(titre, realisateur,genre);

        } catch (GenreNotFoundException e) {
            this.fireOrdre(TypeOrdre.ERREUR_GENRE_INEXISTANT);
            this.fireOrdre(TypeOrdre.DO_VIDER_CHAMPS);
            this.fireOrdre(TypeOrdre.SHOW_AJOUT);
        }
        catch ( NomFilmDejaExistantException e) {
            this.fireOrdre(TypeOrdre.ERREUR_FILM_DEJA_EXISTANT);
            this.fireOrdre(TypeOrdre.DO_VIDER_CHAMPS);
            this.fireOrdre(TypeOrdre.SHOW_AJOUT);
        }
    }


    @Override
    public void abonnement(EcouteurOrdre ecouteurOrdre, TypeOrdre... types) {
/*        for (TypeOrdre typeOrdre : types){
            this.abonnes.get(typeOrdre).add(ecouteurOrdre);
        }
        Equivalent à ce qu'il y a ci-dessous */
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
