import java.util.List;

public class Ajoutables{

    public static <T extends Ajoutable<T>> T somme(List<T> liste){

        if(liste.size()==0){return null;}

        T res = liste.get(0);

        for (int i=1;i<liste.size(); i++){
            res=res.ajoute(liste.get(i));
        }
        return res;
    }
}