import org.junit.Assert;
import org.junit.Test;
import java.util.List;
import java.util.ArrayList;

public class IntersectionTest{

    @Test
    public void intersectionVideRenvoieVide() {
        List<Integer> l1 = new ArrayList<Integer>(); 
        List<Integer> l2 = new ArrayList<Integer>(); 
        List<Integer> res = BibDM.intersection(l1,l2);
        Assert.assertTrue("L'intersection de deux Listes vides doit être une Liste vide", res!= null && res.isEmpty() );
    }

    @Test
    public void interesectionDeuxListesEgalesRenvoieListe() {
        List<Integer> l1 = new ArrayList<Integer>(); 
        l1.add(5);
        l1.add(6);
        l1.add(7);
        List<Integer> l2 = new ArrayList<Integer>(); 
        l2.add(5);
        l2.add(6);
        l2.add(7);
        List<Integer> res = BibDM.intersection(l1,l2);
        Assert.assertTrue("L'intersection de [5,6,7] avec [5,6,7] est [5,6,7]", res!=null && res.equals(l1));
    }
    @Test
    public void initersectionListeAvecDuplicatsRenvoieListeSansDuplicats() {
        List<Integer> l1 = new ArrayList<Integer>(); 
        l1.add(5);
        l1.add(5);
        l1.add(5);
        List<Integer> res = BibDM.intersection(l1,l1);
        List<Integer> l2 = new ArrayList<Integer>(); 
        l2.add(5);
        Assert.assertTrue("L'intersection de [5,5,5] avec [5,5,5] est [5]", res!=null && res.equals(l2));
    }

    @Test
    public void intersectionExemple() {
        List<String> l1 = new ArrayList<>(); 
        l1.add("ami");
        l1.add("bonjour");
        l1.add("dromadaire");
        l1.add("elephant");
        l1.add("fromage");
        l1.add("gateau");
        List<String> l2 = new ArrayList<>(); 
        l2.add("bonjour");
        l2.add("camion");
        l2.add("elephant");
        l2.add("faon");
        l2.add("gateau");
        List<String> res = BibDM.intersection(l1,l2);
        List<String> l3 = new ArrayList<>(); 
        l3.add("bonjour");
        l3.add("elephant");
        l3.add("gateau");
        Assert.assertTrue("L'intersection de "+l1+ " avec "+l2+ " doit donner " +l3 , res!=null && res.equals(l3));
    }
    @Test(timeout=2000)
    public void intersectionDoitEtreEnTempsLineaire() {
        List<Integer> l1 = new ArrayList<Integer>(); 
        List<Integer> l2 = new ArrayList<Integer>(); 
        for(int i =0; i<100000; i++){
            l1.add(i);
            l2.add(100000+i);
        }
        List<Integer> res = BibDM.intersection(l1,l2);
        Assert.assertTrue("L'intersection sur deux listes [1,2,3,...,100000] et [100001,...] est vide", res!= null && res.isEmpty() );
    }

}
