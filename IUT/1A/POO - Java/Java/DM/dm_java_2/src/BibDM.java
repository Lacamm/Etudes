import java.util.Collections;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays; // classe permettant de convertir et trier des tableaux
import java.util.Set; // interface implémentant HashSet
import java.util.HashSet; // classe permettant de créer une HashMap en n'autorisant pas les doublons
public class BibDM{

    /**
     * Ajoute deux entiers
     * @param a le premier entier à ajouter
     * @param b le deuxieme entier à ajouter
     * @return la somme des deux entiers
     */
    public static Integer plus(Integer a, Integer b){
        return a+b;
    }


    /**
     * Renvoie la valeur du plus petit élément d'une liste d'entiers
     * VOUS DEVEZ LA CODER SANS UTILISER COLLECTIONS.MIN (i.e. vous devez le faire avec un for)
     * @param liste
     * @return le plus petit élément de liste
     */
    public static Integer min(List<Integer> liste){
        Integer min = null;
        for (Integer elem: liste){
            if (min==null || min > elem){
                min = elem;
            }
        }
        return min;
    }
    
    
    /**
     * Teste si tous les élements d'une liste sont plus petits qu'une valeure donnée
     * @param valeur 
     * @param liste
     * @return true si tous les elements de liste sont plus grands que valeur.
     */
    public static<T extends Comparable<? super T>> boolean plusPetitQueTous( T valeur , List<T> liste){
        boolean res;
        res = true;
        for (T elem: liste){
            if (valeur.compareTo(elem) >= 0){
                res = false;
            }
        }
        return res;
    }


    /**
     * Intersection de deux listes données par ordre croissant.
     * @param liste1 une liste triée
     * @param liste2 une liste triée
     * @return une liste triée avec les éléments communs à liste1 et liste2
     */
    public static <T extends Comparable<? super T>> List<T> intersection(List<T> liste1, List<T> liste2){
        Set<T> set1 = new HashSet<>(liste1); // Création de Hash pour éviter d'avoir des valeurs en doublons pour chaque liste
        Set<T> set2 = new HashSet<>(liste2);
        set2.retainAll(set1); // Garde dans set2 uniquement les valeurs aussi présentes dans set1

        List<T> res = new ArrayList<>(set2);
        Collections.sort(res);
        return res;

    }

    /**
     * Découpe un texte pour obtenir la liste des mots le composant. texte ne contient que des lettres de l'alphabet et des espaces.
     * @param texte une chaine de caractères
     * @return une liste de mots, correspondant aux mots de texte.
     */
    public static List<String> decoupe(String texte){

        List<String> res = new ArrayList<>();
        if (texte.length()==0){return res;}

        String texteSansEspace = new String(texte.replaceAll("\\s+", " ")); //suppression des espaces
        if (texteSansEspace.charAt(0)==' '){
            String newTexteSansEspace = texteSansEspace.substring(1, texteSansEspace.length()-1); //découpage des mots sans espaces
            return Arrays.asList(newTexteSansEspace.split(" ")); // répartition des mots dans une liste
        }
        return Arrays.asList(texteSansEspace.split(" "));// répartition des mots dans une liste
    }


    /**
     * Renvoie le mot le plus présent dans un texte.
     * @param texte une chaine de caractères
     * @return le mot le plus présent dans le texte. En cas d'égalité, renvoyer le plus petit dans l'ordre alphabétique
     */

    public static String motMajoritaire(String texte){

        if (texte.length()==0){return null;}

        List<String> listeMots = new ArrayList<>();
        listeMots = BibDM.decoupe(texte);
        int max = Collections.frequency(listeMots, listeMots.get(0));
        String res = listeMots.get(0);

        for (int i =1;i<listeMots.size()-1;i++){
          if (Collections.frequency(listeMots, listeMots.get(i))>=max){
                res = listeMots.get(i);
            }
          }
        return res;
    }
    
    /**
     * Permet de tester si une chaine est bien parenthesée
     * @param chaine une chaine de caractères composée de ( et de )
     * @return true si la chaine est bien parentjèsée et faux sinon. Par exemple ()) est mal parenthèsée et (())() est bien parenthèsée.
     */
    public static boolean bienParenthesee(String chaine){
        int cptPO = 0;
        int cptPF = 0;
        boolean res = true;
        for (int i=0; i<chaine.length();i++){
            if (chaine.charAt(i) == '(' ){cptPO+=1;}
            else if (chaine.charAt(i) == ')' ){cptPF+=1;}

            if (cptPF > cptPO){res = false;}
        }
        if (cptPF != cptPO){res = false;}
        return res;
    }
    
    /**
     * Permet de tester si une chaine est bien parenthesée
     * @param chaine une chaine de caractères composée de (, de  ), de [ et de ]
     * @return true si la chaine est bien parentjèsée et faux sinon. Par exemple ([)] est mal parenthèsée alors ue ([]) est bien parenthèsée.
     */
    public static boolean bienParentheseeCrochets(String chaine){
        int cptPO = 0;
        int cptPF = 0;
        int cptCO = 0;
        int cptCF = 0;

        boolean res = true;
        for (int i=0; i<chaine.length();i++){
            if (chaine.charAt(i) == '(' ){cptPO+=1;}
            else if (chaine.charAt(i) == ')' ){cptPF+=1;}
            else if (chaine.charAt(i) == '[' ){cptCO+=1;}
            else if (chaine.charAt(i) == ']' ){cptCF+=1;}

            if (cptPF > cptPO || cptCF > cptCO ){res = false;}

            if (cptCO < cptPO && cptPF != cptPO && cptCF == cptCO){res = false;}
            else if(cptCF > cptPF && cptPF != cptPO && cptCF == cptCO){res = false;}
        }
        if (cptPF != cptPO || cptCF != cptCO){res = false;}
        return res;

    }


    /**
     * Recherche par dichtomie d'un élément dans une liste triée
     * @param liste, une liste triée d'entiers
     * @param valeur un entier
     * @return true si l'entier appartient à la liste.
     */
    public static boolean rechercheDichotomique(List<Integer> liste, Integer valeur){
        boolean res;

        if (liste.isEmpty()){res = false;}
        else{
            int indiceDebut, indiceFin, indiceMilieu;

            indiceDebut = 0;
            indiceFin = liste.size()-1;
            res = false;

            while (!res && (indiceDebut <= indiceFin)){
                indiceMilieu = (indiceDebut + indiceFin) / 2;
                if (valeur == liste.get(indiceMilieu)){res = true;}
                else if (valeur > liste.get(indiceMilieu)){indiceDebut = indiceMilieu +1;}
                else {indiceFin = indiceMilieu -1;}
            }
        }
        return res;
    }



}
