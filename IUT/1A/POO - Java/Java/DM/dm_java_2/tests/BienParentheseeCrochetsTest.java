import org.junit.Assert;
import org.junit.Test;
import java.util.List;
import java.util.ArrayList;

public class BienParentheseeCrochetsTest{
    @Test
    public void chaineVideBienParenthesee() {
        Assert.assertTrue(BibDM.bienParentheseeCrochets(""));
    }

    @Test
    public void moinsDeParenthesesOuvrantesQueFermantesEstMalParenthesee() {
        Assert.assertFalse(BibDM.bienParentheseeCrochets("(()))"));
        Assert.assertFalse(BibDM.bienParentheseeCrochets("()[]]"));
    }
    
    @Test
    public void pasDansLeBonOrdre() {
        Assert.assertFalse(BibDM.bienParentheseeCrochets(")("));
        Assert.assertFalse(BibDM.bienParentheseeCrochets("()())()("));
        Assert.assertFalse(BibDM.bienParentheseeCrochets("([)]"));
        Assert.assertFalse(BibDM.bienParentheseeCrochets("()[(])"));
        Assert.assertFalse(BibDM.bienParentheseeCrochets("()[[(]])"));
    }

    @Test
    public void moinsDeParenthesesFermantesQueOuvrantesEstMalParenthesee() {
        Assert.assertFalse(BibDM.bienParentheseeCrochets("((())"));
        Assert.assertFalse(BibDM.bienParentheseeCrochets("[[[]]()"));
    }

    @Test
    public void unExempleBienParenthese() {
        Assert.assertTrue(BibDM.bienParentheseeCrochets("()()()(())"));
        Assert.assertTrue(BibDM.bienParentheseeCrochets("[[()]][()]([][]())"));
    }




}
