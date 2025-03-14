import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.control.Button;
import javafx.scene.layout.Background;
import javafx.scene.layout.BackgroundFill;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Color;

import java.util.ArrayList;

/**
 * Génère la vue d'un clavier et associe le contrôleur aux touches
 * le choix ici est d'un faire un héritié d'un GridPane
 */
public class Clavier extends GridPane{
    /**
     * il est conseillé de stocker les touches dans un ArrayList
     */
    private ArrayList<Button> clavier;

    /**
     * constructeur du clavier
     * @param touches une chaine de caractères qui contient les lettres à mettre sur les touches
     * @param actionTouches le contrôleur des touches
     * @param tailleLigne nombre de touches par ligne
     */
    public Clavier(String touches, EventHandler<ActionEvent> actionTouches, int tailleLigne) {
        this.clavier = new ArrayList<>();
        this.setHgap(1);
        this.setVgap(1);
        this.setAlignment(Pos.CENTER);
        this.setPadding(new Insets(10));
        int ligne = 0;
        for (int i = 0; i < touches.length(); i++) {

            Button b = new Button(Character.toString(touches.charAt(i)));
            this.clavier.add(b);

            if (i % tailleLigne == 0) { ligne++; }

            super.add(b, i % tailleLigne, ligne);
            b.setOnAction(actionTouches);
            this.setAlignment(Pos.CENTER);

            b.setPrefWidth(50);
            b.setPadding(new Insets(5, 5, 5, 5));
        }
    }

    /**
     * permet de désactiver certaines touches du clavier (et active les autres)
     * @param touchesDesactivees une chaine de caractères contenant la liste des touches désactivées
     */
    public void desactiveTouches(String touchesDesactivees){
        for (Button b: this.clavier) {
            if (touchesDesactivees.contains(b.getText())) {
                b.setDisable(true);
                b.setBackground(new Background(new BackgroundFill(Color.GRAY, null, null)));
            }else{
                b.setDisable(false);
                b.setBackground(new Background(new BackgroundFill(Color.LIGHTBLUE, null, null)));
            }
        }
    }
}
