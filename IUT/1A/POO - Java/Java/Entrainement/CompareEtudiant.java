import java.util.*;

public class CompareEtudiant implements Comparator<Etudiant> {

    public int compare(Etudiant e1, Etudiant e2) {
        Integer v1 = e1.getTelepathie() + e1.getPrecognition()/2;
        Integer v2 = e2.getTelepathie() + e2.getPrecognition()/2;
        return v2.compareTo(v1);
    }
}