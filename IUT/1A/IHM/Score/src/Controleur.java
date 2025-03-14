import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.Label;

public class Controleur implements EventHandler<ActionEvent> {
    private Vue vue;
    private Scores scores;
    public ObservableList<String> obList;

    public Controleur(Vue vue) {
        this.vue = vue;
        this.scores = new Scores(5);
    }

    @Override
    public void handle(ActionEvent actionEvent) {
        Button b = (Button) actionEvent.getSource();
        try {
            Integer point = Integer.parseInt(this.vue.getNbPoints().getText());
            String nom = this.vue.getNomJoueur().getText();
            if (!nom.equals("")) {
                if (this.scores.ajouterScore(nom, point)) {
                    this.vue.getNbPoints().clear();
                    this.vue.getNomJoueur().clear();
                    this.obList = FXCollections.observableArrayList();
                    for (int i = 0; i < this.scores.getNbScore(); i++) {
                        this.obList.add(this.scores.getScores(i));
                    }
                    this.vue.getTableau().setItems(this.obList);
                }
                else{
                    Alert al = new Alert(Alert.AlertType.ERROR);
                    al.setTitle("Attention !!!");
                    al.setHeaderText("Score pas assez élevé !");
                    al.setContentText("Le score n'est pas assez élevé pour être dans le top 5");
                    al.showAndWait();
                    this.vue.getNbPoints().clear();
                    this.vue.getNomJoueur().clear();
                }
            }
            else{
                Alert al = new Alert(Alert.AlertType.ERROR);
                al.setTitle("Attention !!!");
                al.setHeaderText("Mauvais type champ 1 !");
                al.setContentText("Le nom doit contenir au moins un caractère");
                al.showAndWait();

            }
        } catch (NumberFormatException e) {
            Alert al = new Alert(Alert.AlertType.ERROR);
            al.setTitle("Attention !!!");
            al.setHeaderText("Mauvais type champ 2 !");
            al.setContentText("Il faut rentrer des nombres entiers");
            al.showAndWait();
        }
    }
}