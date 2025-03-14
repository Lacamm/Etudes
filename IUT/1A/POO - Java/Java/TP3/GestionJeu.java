import java.util.ArrayList;

public class GestionJeu {

    private Vaisseau vaisseau;
    private ArrayLit<Projectile> lesProjectiles;

    public GestionJeu(){
        this.vaisseau = new Vaisseau();
        this.lesProjectiles = new ArrayList<Projectile>();
    }

    public int getHauteur(){return 60;}
    public int getLargeur(){return 100;}

    public void toucheGauche(){
        vaisseau.deplace(-1);
    }
    public void toucheDroite(){
        vaisseau.deplace(1);
    }
    public void toucheEspace(){
        System.out.println("Appui sur la touche espace");
    }

    public EnsembleChaines getChaines(){
        EnsembleChaines ensVaisseau = this.vaisseau.getEnsembleChaines();
        EnsembleChaines ensProjectiles = this.lesProjectiles.getEnsembleChaines();
        for(Projectile project:lesProjectiles){
            ensProjectiles.union(project);
        }
        ensChaines.union(ensProjectiles,ensVaisseau);
        return ensChaines;
    }
    public void jouerUnTour(){}
}