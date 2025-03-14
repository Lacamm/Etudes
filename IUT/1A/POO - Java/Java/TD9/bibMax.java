import java.util.Collections;
import java.util.List;

public class bibMax {

    public static Integer sommeMax( List<List<Integer>> LL){
        Integer res = 0;
        for ( List<Integer> liste: LL){
            if (liste.size() != 0){
                res += Collections.max(liste); // pareil mutliplication *=
            }
        }
        return res;
    }
}