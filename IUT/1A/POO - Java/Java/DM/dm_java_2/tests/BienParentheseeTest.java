import org.junit.Assert;
import org.junit.Test;
import java.util.List;
import java.util.ArrayList;

public class BienParentheseeTest{
    @Test
    public void chaineVideBienParenthesee() {
        Assert.assertTrue(BibDM.bienParenthesee(""));
    }

    @Test
    public void moinsDeParenthesesOuvrantesQueFermantesEstMalParenthesee() {
        String s;
        s="(()))";
        Assert.assertFalse(s + " est mal parenthesée.", BibDM.bienParenthesee(s));
    }
    
    @Test
    public void pasDansLeBonOrdre() {
        String s;
        s=")(";
        Assert.assertFalse(s + " est mal parenthesée.", BibDM.bienParenthesee(s));
        s = "()())()(";
        Assert.assertFalse(s + " est mal parenthesée.", BibDM.bienParenthesee(s));
    }

    @Test
    public void moinsDeParenthesesFermantesQueOuvrantesEstMalParenthesee() {
        String s = "((())";
        Assert.assertFalse(s + " est mal parenthesée.", BibDM.bienParenthesee(s));
    }

    @Test
    public void exempleBienParenthese() {
        String s="()()()(())";
        Assert.assertTrue(s + " est bien parenthesée", BibDM.bienParenthesee(s));
    }


}
