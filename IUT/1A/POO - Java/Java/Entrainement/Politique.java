import java.util.*;

public class Politique implements Etablissement{

    private String nom;

    public Politique(String nom){
        this.nom = nom;
    }

    @Override
    public int getNbPlaces(){return 1;}

    @Override
    public List<Etudiant> getSelection(List<Etudiant> lesEtu){
        List<Etudiant> tmp = new ArrayList<>(lesEtu);
        Collections.sort(tmp, new CompareEtudiant());
        return tmp;
    }

    public String toString(){return this.nom;}

}