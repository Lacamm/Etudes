import java.util.ArrayList;
import java.util.Collections;
class Bibcollection{
   public static void inverserListe(ArrayList<?> liste){
       Integer indiceMin = 0;
       Integer indiceMax = liste.size()-1;
       while (indiceMin < indiceMax){
           Collections.swap(liste,indiceMin,indiceMax);
           indiceMin+=1;
           indiceMax+=-1;
       }
   }
   public static int freqListe(ArrayList<?> liste){
       return Collections.frequency(liste,liste.get(0));
   }
}