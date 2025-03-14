import java.util.HashMap;
import java.lang.Number;

public class dico{

    public static boolean recetttePossible(HashMap<String, Number> magasin, HashMap<String, Number> recette){
        boolean ok =false;
        int cpt = 0;
        for(String ingredient: recette.keySet()){
            Number val = recette.get(ingredient);
            if(magasin.containsKey(ingredient)){
                if (magasin.get(ingredient).intValue() >= val.intValue()){
                    cpt+=1;
                }
            }
        }
        if (cpt == recette.size()){
            ok = true;
        }
        return ok;
    }

    public static void main (String [] args){

        HashMap<String, Number> recetteCrepe = new HashMap<>();
        HashMap<String, Number> magasin = new HashMap<>();

        recetteCrepe.put("oeufs", 3);
        recetteCrepe.put("farine", 0.25);
        recetteCrepe.put("lait", 0.5);

        magasin.put("oeufs", 10);
        magasin.put("farine", 1.15);
        magasin.put("lait", 5);
        magasin.put("sucre", 4);

        System.out.println(recetteCrepe);
        System.out.println(magasin);

        System.out.println(recetttePossible(magasin,recetteCrepe));

    }
}