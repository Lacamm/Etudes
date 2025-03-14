import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.text.Font;
import javafx.stage.Stage;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.*;
import javafx.scene.paint.Color;

import java.io.File;
import java.util.ArrayList;

/**
 * Vue du jeu du pendu
 */
public class Pendu extends Application {
    /*
     * modèle du jeu
     **/
    private MotMystere m;
    /**
     * tableau qui contient les images du jeu
     */
    private ArrayList<Image> lesImages;
    /**
     *les différents contrôles qui seront mis à jour
     * ou consultés pour l'affichage
     */
    /**
     * le dessin
     */
    private ImageView dessin;
    /**
     * le mot à trouver avec les lettres déjà trouvé
     */
    private Label motCrypte;
    /**
     * la barre de progression qui indique le nombre de tentatives
     */
    private ProgressBar pg;
    /**
     * le clavier qui sera géré par une classe à implémenter
     */
    private Clavier clavier;
    /**
     * le chronomètre qui sera géré par une clasee à implémenter
     */
    private Chronometre chrono;
    /**
     * les radio boutons gérant les niveaux
     */
    ArrayList<RadioButton> niveaux;


	/**
	 * @return le panel du chronomètre
	 */
    private VBox leChrono(){
    	VBox res = new VBox(5);
	// A implémenter
    	return res;
	}


    /**
     * @return le panel des niveaux avec les radio boutons
     */
    private VBox lesNiveaux(){
    	VBox res=new VBox(5);
	// A implémenter
    	return res;
    }


    /**
     * @return le panel central avec le mot crypté, l'image, la barre
     *         de progression et le bouton rejouer
     */
    private VBox central(){
    	VBox res=new VBox(5);
	// A implémenter
    	return res;
	}

    /**
     * @return le panel contenant le titre du jeu
     */
	private FlowPane titre(){
	    FlowPane res = new FlowPane();
	    // A implémenter
	    return res;
	}

    /**
     * @return  le clavier avec les 27 caractères et le controleur des touches
     */
	private Clavier leClavier(){
	    // A Implementer
	    return this.clavier;
       }

    /**
     * @return  le graphe de scène de la vue à partir de methodes précédantes
     */
	private Scene laScene(){
	    BorderPane cont = new BorderPane();
	    cont.setTop(this.titre());
	    cont.setRight(this.lesNiveaux());
	    cont.setCenter(this.central());
	    cont.setBottom(this.leClavier());
	    cont.setLeft(leChrono());
	    return new Scene(cont,700,800);
	}


    /**
     * charge les images à afficher en fonction des erreurs
     * @param repertoire répertoire où se trouvent les images
     */
	private void chargerImages(String repertoire){
		this.lesImages= new ArrayList<Image>();
		for (int i=0;i<m.getNbErreursMax()+1;i++){
		    File file = new File(repertoire+"/pendu"+i+".png");
		    System.out.println(file.toURI().toString());
			this.lesImages.add(new Image(file.toURI().toString()));
		}
	}

    /**
     * Affiche en clair le mot à trouver
     */
	public void afficheReponse(){
	    // A implémenter
	}

    /**
     * raffraichit l'affichage en fonction du modèle
     */
	public void majAffichage(){
	    // A implémenter
	}

    /**
     * accesseur du chronomètre (pour les controleur du jeu)
     * @return le chronomètre du jeu
     */
	public Chronometre getChrono(){
	    // A implémenter
	    return null; // A enlever
	}

    public void activerNiveau(boolean actif) {
        // A implémenter
    }

    /**
     * Crée le modèle, charge les images, créer le graphe de scène et lance le jeu
     * @param stage la fenêtre principale
     */
	@Override
	public void start(Stage stage) {
	    // création du modèle
	    m=new MotMystere("/usr/share/dict/french",3,10,MotMystere.PREMIEREETDERNIERE,10);
	    // Chargement des images
	    this.chargerImages("./img");
	    stage.setTitle("Jeu du pendu");
	    stage.setScene(this.laScene());
	    stage.show();
	    // démarrage du chrono
	    this.chrono.start();
	}

    /**
     * Programme principal
     * @param args inutilisé
     */
    public static void main(String[] args) {
        launch(args);
    }

}
