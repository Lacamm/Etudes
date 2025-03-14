import org.junit.Assert;
import org.junit.Test;
import java.util.List;
import java.util.ArrayList;

public class MotMajoritaireTest{
    @Test
    public void majoritaireTexteVideEstNull() {
        Assert.assertNull(BibDM.motMajoritaire(""));
    }

    @Test
    public void majoritaireTexteExemple() {
        Assert.assertEquals("ami", BibDM.motMajoritaire("ami bonjour tambour ami toto"));
    }

    @Test
    public void majoritaireTexteExempleAvecEspaces() {
        Assert.assertEquals("ami", BibDM.motMajoritaire(" ami bonjour tambour    ami  toto   "));
    }
    @Test
    public void majoritairePremierParOrdreAlphabetiqueEnCasDEgalite() {
        Assert.assertEquals("ami", BibDM.motMajoritaire("bonjour ami zut bonjour ami zut"));
    }

    @Test(timeout=2000)
    public void majoritaireDoitEtreEfficace() {
        String texte = "";        
        for(int i =0; i<10000; i++){
            texte = texte + "a ";
            texte = texte + "b ";

        }
        texte = texte + "a";
        Assert.assertEquals("a", BibDM.motMajoritaire(texte));
    }
}
