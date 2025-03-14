import org.junit.Assert;
import org.junit.Test;
import org.junit.BeforeClass;
import java.util.List;
import java.util.ArrayList;
public class RechercheDichotomiqueTest{
    static ArrayList<Integer> tab0;
    static ArrayList<Integer> tab1;
    static ArrayList<Integer> tab2;
    static ArrayList<Integer> tab3;
    @BeforeClass
    public static void init(){
        tab0 = new ArrayList<Integer>();
        tab0.add(1);
        tab0.add(2);
        tab0.add(3);
        tab0.add(4);
        tab1 = new ArrayList<Integer>();
        for(int i=0;i<100000;i++)
            tab1.add(i-50000);
        tab2 = new ArrayList<Integer>();
        tab3 = new ArrayList<Integer>();
        for(int i=0;i<100000;i++)
            tab3.add(-100);
    }
    @Test(timeout=1)
    public void rechercheCorrecteSurPetitTableau() {
        Assert.assertTrue("1 appartient au tableau [1,2,3,4]. Votre fonction dit le contraire",BibDM.rechercheDichotomique(tab0,1));
        Assert.assertTrue("2 appartient au tableau [1,2,3,4]. Votre fonction dit le contraire",BibDM.rechercheDichotomique(tab0,2));
        Assert.assertTrue("3 appartient au tableau [1,2,3,4]. Votre fonction dit le contraire",BibDM.rechercheDichotomique(tab0,3));
        Assert.assertTrue("4 appartient au tableau [1,2,3,4]. Votre fonction dit le contraire",BibDM.rechercheDichotomique(tab0,4));
        Assert.assertFalse("0 n'appartient pas au tableau [1,2,3,4]. Votre fonction dit le contraire",BibDM.rechercheDichotomique(tab0,0));
    }
    @Test(timeout=1)
    public void rechercheSurGrosTableau() {
        Assert.assertFalse(BibDM.rechercheDichotomique(tab1,30000000));
        Assert.assertTrue(BibDM.rechercheDichotomique(tab1,0));
    }
    @Test(timeout=1)
    public void rechercheSurListeVideDoitRenvoyerFalse(){
        Assert.assertFalse(BibDM.rechercheDichotomique(tab2,10));
    }
}
