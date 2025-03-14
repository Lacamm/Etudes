import java.util.*;

public class BTP implements Etablissement{

    private int nbPlaces;
    private String nom;

    public BTP(String nom, int nbPlaces){
        this.nbPlaces = nbPlaces;
        this.nom = nom;
    }

    @Override
    public int getNbPlaces(){return this.nbPlaces;}

    @Override
    public List<Etudiant> getSelection(List<Etudiant> lesEtu){
        List<Etudiant> tmp = new ArrayList<>(lesEtu);
        Collections.sort(tmp);
        return tmp;
    }

    public String toString(){return this.nom;}

}