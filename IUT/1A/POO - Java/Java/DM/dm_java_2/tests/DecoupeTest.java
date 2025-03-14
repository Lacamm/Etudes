import org.junit.Assert;
import org.junit.Test;
import java.util.List;
import java.util.ArrayList;

public class DecoupeTest{

    @Test
    public void DecoupeChaineVideRenvoieListeVide() {
        List<String> liste = new ArrayList<String>();
        Assert.assertEquals(liste, BibDM.decoupe(""));
    }

    @Test
    public void DecoupeExemple() {
        List<String> liste = new ArrayList<String>();
        liste.add("Bonjour");
        liste.add("tout");
        liste.add("le");
        liste.add("monde");
        Assert.assertEquals(liste, BibDM.decoupe("Bonjour tout le monde"));
    }
    @Test
    public void DecoupeEspacesMultiplesExemple() {
        List<String> liste = new ArrayList<String>();
        liste.add("Bonjour");
        liste.add("tout");
        liste.add("le");
        liste.add("monde");
        Assert.assertEquals(liste, BibDM.decoupe("  Bonjour  tout le     monde "));
    }
}
