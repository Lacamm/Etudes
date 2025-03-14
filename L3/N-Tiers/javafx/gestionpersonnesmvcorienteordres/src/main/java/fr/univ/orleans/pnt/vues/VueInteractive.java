package fr.univ.orleans.pnt.vues;

import fr.univ.orleans.pnt.controleur.Controleur;

public interface VueInteractive {

    void setControleur(Controleur controleur);
    Controleur getControleur();

}
