import org.junit.Assert;
import org.junit.Test;
import java.util.List;
import java.util.ArrayList;

public class MinTest{

    @Test
    public void MinListeVideEstNull(){
        List<Integer> liste = new ArrayList<>();
        Assert.assertNull("Sur une liste vide, il faut renvoyer null", BibDM.min(liste));
    }

    @Test
    public void MinListeExemple() {
        List<Integer> liste = new ArrayList<>();
        liste.add(-5);
        liste.add(10);
        liste.add(-7);
        Assert.assertEquals("Le plus petit element de la liste [-5,10,-7] est -7", (Integer)BibDM.min(liste), new Integer(-7));
    }
}
