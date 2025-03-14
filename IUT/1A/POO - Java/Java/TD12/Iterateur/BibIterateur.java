import java.util.List;
import java.util.Iterator;

public class BibIterateur {

    public static <T> void afficheElem(List<T> liste){
        Iterator<T> iterateur = liste.iterator();
        while(iterateur.hasNext()){
            System.out.println(iterateur.next() + " ");
        }
    }

    public static <T> void afficheTous(Iterable<T> AIterer){
        Iterator<T> iterateur = AIterer.iterator();
        while(iterateur.hasNext()){
            System.out.println(iterateur.next() + " ");
        }
    }

    public static Integer getMin(Iterable<Integer> liste) throws ListeVideException{
        Integer res = null;
        Iterator<Integer> iterateur = liste.iterator();

        if(iterateur.hasNext()){res = iterateur.next();}
        else{throw new ListeVideException();}

        while(iterateur.hasNext()){
            if (iterateur.next() < res){
                res = iterateur.next();
            }
        }
        return res;
    }

    public static Integer somme(Iterable<Integer> liste){
        Integer res = 0;
        Iterator<Integer> iterateur = liste.iterator();
        while(iterateur.hasNext()){
            res+=iterateur.next();
        }
        return res;
    }


    public static int plusLongPlateau(Iterable<Integer> it) throws ListeVideException{
        Iterator<Integer> i = it.iterator();
        Integer prec = null;
        int plusLong = 1;
        int longActuelle = 1;
        Integer courant = null;

        if(!i.hasNext()){throw new ListeVideException();}
        else{
            while(i.hasNext()){
                courant = i.next();
                if(prec != null){
                    if(prec.compareTo(courant) == 0){
                        longActuelle = longActuelle + 1;
                    }
                    else{longActuelle = 1;}
                    if(longActuelle > plusLong){plusLong = longActuelle;}
                }
                prec = courant;
            }
        }
        return plusLong;
    }
    
} 