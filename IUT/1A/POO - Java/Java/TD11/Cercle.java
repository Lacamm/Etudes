import java.util.List;
import java.util.ArrayList;
import javafx.scene.shape.Circle;
import javafx.scene.paint.Color;

public class Cercle extends Circle{

    public Cercle(List<Cercle> liste,int largeur, int hauteur){
        super(Math.random()*600, Math.random()*300,5);
        this.setFill(new Color(Math.random(),Math.random(),Math.random(),1));
        this.grossir(liste,largeur,hauteur);
        this.placerAuHasard(liste,largeur,hauteur);
    }

    public boolean intersecte(Cercle c){
        double ecartCentre;
        ecartCentre = Math.sqrt(Math.pow(c.getCenterX()-this.getCenterX(),2)+Math.pow(c.getCenterY()-this.getCenterY(),2));

        return ecartCentre < c.getRadius()+this.getRadius();
    }
    
    public boolean estDansLeCadre(double largeur, double hauteur){
        return ((this.getCenterX() - this.getRadius()) >= 0 &&
                (this.getCenterX() + this.getRadius()) <= largeur &&
                (this.getCenterY() - this.getRadius()) >= 0 &&
                (this.getCenterY() + this.getRadius()) <= hauteur);
    }

    public boolean estValide(List<Cercle> liste, double largeur, double hauteur){
        boolean res = true;

        for (Cercle c: liste){
            if (this.intersecte(c) || !this.estDansLeCadre(largeur,hauteur)){
                res = false;
            }
        }
        return res;
    }

    public void placerAuHasard(List<Cercle> liste, double largeur, double hauteur){
        while(!this.estValide(liste, largeur, hauteur)){
            this.setCenterX(Math.random()*largeur);
            this.setCenterY(Math.random()*hauteur);
        }
    }

    public void grossir(List<Cercle> liste, double largeur, double hauteur){
        while (this.estValide(liste, largeur, hauteur)){
            this.setRadius(this.getRadius()+10);
        }
    }

}