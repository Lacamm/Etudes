import org.junit.Assert;
import org.junit.Test;
import java.util.List;
import java.util.ArrayList;

public class PlusTest{

    @Test
    public void plus0Et0Renvoie0() {
         Assert.assertEquals((Integer)0, BibDM.plus(0,0));
    }
    
    @Test
    public void plus10Et15Renvoie25() {
         Assert.assertEquals((Integer)25, BibDM.plus(10,15));
    }

}
