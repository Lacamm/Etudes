import javafx.application.Application; 
import javafx.scene.Group; 
import javafx.scene.layout.BorderPane;
import javafx.scene.Scene; 
import javafx.stage.Stage; 
import javafx.scene.paint.Color;
import java.util.List;
import java.util.ArrayList;
import javafx.scene.shape.Circle;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;

public class DessinExemple extends Application {
    
    private  int largeur = 600;
    private  int hauteur = 300;
    
    @Override 
    public void start(Stage stage){ 
       List<Cercle> liste = new ArrayList<>();
       
    // === Code à modifier ===========
        for (int i=0;i<10;i++){
            Cercle c = new Cercle(liste, this.largeur,this.hauteur);
            c.setFill(new Color(Math.random(),Math.random(),Math.random(),1.0));
            liste.add(c);
        }

    // ===============================
    
      Group dessinCercles = new Group();
       dessinCercles.getChildren().addAll(liste);
       
       BorderPane root = new BorderPane();
       root.getChildren().add(dessinCercles);
       VBox vbox =this.informations(liste);
       root.setBottom(vbox);
       Scene scene = new Scene(root, this.largeur, this.hauteur+vbox.getHeight()+40);  
       stage.setTitle("Formes");
       stage.setScene(scene);
       stage.show();         
   }       


    private VBox informations(List<Cercle> liste){
        VBox vbox = new VBox();
        String cssLayout = "-fx-border-color: black;\n" + "-fx-border-width: 2;\n";
        vbox.setStyle(cssLayout);
        // Décommentez et complétez le code ici ======
        
        // vbox.getChildren().add(new Label("Le Cercle le plus petit est : "));
        // vbox.getChildren().add(new Label("La surface totale est : "));  
              
        // ===========================================
        return vbox;      
    }
    public static void main(String args[]){ 
       launch(args); 
   }
}


/*
Question 1:
    Circle(double centreX, double centreY, double rayon)

Question 2:
    setFill() se trouve dans la classe Shape

Question 3:
    Color est une classe qui hérite de Paint

Question 4:
    Color(int rouge ,int vert ,int bleu , int opacité)
*/