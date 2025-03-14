import org.junit.Assert;
import org.junit.Test;
import java.util.List;
import java.util.ArrayList;

public class PlusPetitQueTousTest{

    @Test
    public void bonjourPlusPetitQueToutLeMonde() {
        String s = new String("bonjour");
        List<String> liste = new ArrayList<String>();
        liste.add("tout");
        liste.add("le");
        liste.add("monde");
        Assert.assertTrue("Votre fonction a renvoyé False avec le mot bonjour et la liste [\"tout\", \"le\", \"monde\" ]. Elle aurait du renvoyer True ", BibDM.plusPetitQueTous(s,liste));
    }

    @Test
    public void lePasPlusPetiteQueToueLeMonde() {
        String s = new String("le");
        List<String> liste = new ArrayList<String>();
        liste.add("tout");
        liste.add("le");
        liste.add("monde");
        Assert.assertFalse("Votre fonction a renvoyé True avec le mot \"le\" et la liste [\"tout\", \"le\", \"monde\" ]. Elle aurait du renvoyer False", BibDM.plusPetitQueTous(s,liste));
    }

    @Test
    public void zozoPasPlusPetitQueToutLeMonde() {
        String s = new String("zozo");
        List<String> liste = new ArrayList<String>();
        liste.add("tout");
        liste.add("le");
        liste.add("monde");
        Assert.assertFalse("Votre fonction a renvoyé True avec le zozo le et la liste [\"tout\", \"le\", \"monde\" ]. Elle aurait du renvoyer False", BibDM.plusPetitQueTous(s,liste));
    }

    @Test
    public void bonjourPlusPetitQueElemsDeListeVide() {
        String s = new String("bonjour");
        List<String> liste = new ArrayList<String>();
        Assert.assertTrue("Votre fonction a renvoyé False avec le mot bonjour et une liste vide. Elle aurait du renvoyer True.", BibDM.plusPetitQueTous(s,liste));
    }
}