import java.util.*;

public class Attribution{

    public static Map<Etudiant,List<Etudiant>> listePrincipale(List<Etudiant> etudiants, List<Etablissement>listeEcoles){
        Map<Etudiant, List<Etablissement>> principale = new HashMap<>();
        List<Etudiant> selection = null;
        Etudiant etudiant = null;
        for (Etablissement ecole: listeEcoles){
            selection = ecole.getSelection(etudiants);
            for(int i = 0; i<ecole.getNbPlaces();i++){
                etudiant = selection.get(i);
                if(!principale.containsKey(etudiant)){
                    principale.put(etudiant, new ArrayList<>());
                }
                principale.get(etudiant).add(ecole);
            }
        }
    }
}