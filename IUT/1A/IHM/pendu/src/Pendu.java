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
    private Chronometre chrono = new Chronometre();
    /**
     * les radio boutons gérant les niveaux
     */
    private ArrayList<RadioButton> niveaux;

	private ToggleGroup tg;


	/**
	 * @return le panel du chronomètre
	 */
    private VBox leChrono(){
    	VBox res = new VBox(5);
    	Label l = new Label("Chronomètre");
    	res.getChildren().addAll(l, this.chrono);
		res.setAlignment(Pos.CENTER);
		res.setStyle("-fx-background-color: #23c0e0;");
    	return res;
	}

    /**
     * @return le panel des niveaux avec les radio boutons
     */
    private VBox lesNiveaux(){
    	VBox res=new VBox(5);
    	Label l = new Label("Les Niveaux");
    	RadioButton facile = new RadioButton("Facile");
		RadioButton medium = new RadioButton("Medium");
		RadioButton difficile = new RadioButton("Difficile");
		RadioButton expert = new RadioButton("Expert");

		this.niveaux = new ArrayList<>();

		this.niveaux.add(facile);
		this.niveaux.add(medium);
		this.niveaux.add(difficile);
		this.niveaux.add(expert);

		facile.setId("0");
		medium.setId("1");
		difficile.setId("2");
		expert.setId("3");

		activerNiveau(false);

		facile.setOnAction(new ItemNiveau(this.m,this));
		medium.setOnAction(new ItemNiveau(this.m,this));
		difficile.setOnAction(new ItemNiveau(this.m,this));
		expert.setOnAction(new ItemNiveau(this.m,this));

		this.tg= new ToggleGroup();

		facile.setToggleGroup(this.tg);
		medium.setToggleGroup(this.tg);
		difficile.setToggleGroup(this.tg);
		expert.setToggleGroup(this.tg);

		facile.setSelected(true);

		res.getChildren().addAll(l,facile, medium, difficile, expert);
		res.setAlignment(Pos.CENTER_LEFT);
		res.setStyle("-fx-background-color: #23c0e0;");

    	return res;
    }

	public int getNiveaux(){
		String res ="";
		res = ((RadioButton) this.tg.getSelectedToggle()).getText();
		if (res.equals("Facile")) return 0;
		else if(res.equals("Moyen")) return 1;
		else if(res.equals("Difficile")) return 2;
		else if(res.equals("Expert")) return 3;
		return 4;
	}


    /**
     * @return le panel central avec le mot crypté, l'image, la barre
     *         de progression et le bouton rejouer
     */
    private VBox central(){
    	VBox res=new VBox(5);

		this.motCrypte = new Label(this.m.getLettresTrouvees());
		this.dessin = new ImageView(this.lesImages.get(0));
		this.pg = new ProgressBar(0);

		Button b = new Button("Rejouer");
		b.setOnAction(new ActionRejouer(m, this));

		res.getChildren().addAll(this.motCrypte,this.dessin,this.pg,b);
		res.setAlignment(Pos.CENTER);
		res.setStyle("-fx-background-color: #4863f9;");
    	return res;
	}

    /**
     * @return le panel contenant le titre du jeu
     */
	private FlowPane titre(){
	    FlowPane res = new FlowPane();
	    Label titre = new Label("Le jeu du Pendu");
		titre.setFont(new Font(50));
	    res.getChildren().addAll(titre);
	    res.setAlignment(Pos.CENTER);
		res.setStyle("-fx-background-color: #23c0e0;");
	    return res;
	}

    /**
     * @return  le clavier avec les 27 caractères et le controleur des touches
     */
	private Clavier leClavier(){
		ActionLettre actionL = new ActionLettre(m, this);
		clavier = new Clavier("AZERTYUIOPQSDFGHJKLMWXCVBN-", actionL,9);
		this.clavier.setStyle("-fx-background-color: #23c0e0;");
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
	public void afficheReponse(){this.motCrypte.setText(this.m.getMotATrouve());
	}

    /**
     * raffraichit l'affichage en fonction du modèle
     */
	public void majAffichage() {
		this.clavier.desactiveTouches(this.m.getLettresEssayees());
		this.dessin.setImage(this.lesImages.get(m.getNbErreursMax() - m.getNbErreursRestants()));
		this.motCrypte.setText(m.getLettresTrouvees());
		this.setPg();
	}


	public void setPg(){
		String var = m.getMotATrouve();
		double nblettre = (double) var.length();
		double lTrouve = (double) m.getNbLettresRestantes();
		lTrouve = nblettre-lTrouve;
		this.pg.setProgress(lTrouve/nblettre);
	}

    /**
     * accesseur du chronomètre (pour les controleur du jeu)
     * @return le chronomètre du jeu
     */
	public Chronometre getChrono(){
	    return this.chrono;
	}

    public void activerNiveau(boolean actif) {
		for(RadioButton button:this.niveaux) {
			button.setDisable(!actif);
		}
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
		this.majAffichage();
	}

    /**
     * Programme principal
     * @param args inutilisé
     */
    public static void main(String[] args) {
        launch(args);
    }

}
