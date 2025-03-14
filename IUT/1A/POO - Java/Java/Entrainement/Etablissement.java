import java.util.*;

public interface Etablissement{

    public int getNbPlaces();
    public List<Etudiant> getSelection(List<Etudiant> lesEtu);
}