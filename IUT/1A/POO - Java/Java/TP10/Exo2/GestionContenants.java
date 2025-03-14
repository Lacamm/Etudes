import java.util.List;
import java.util.ArrayList;

public class GestionContenants{
    public static <T> boolean contiennentTous(List<Contenant<T>> conts, T elem){
        boolean res = true;
        for (Contenant<T> c: conts){
            if(! c.contient(elem)){
                res = false;
            }
        }
        return res;
    }
}