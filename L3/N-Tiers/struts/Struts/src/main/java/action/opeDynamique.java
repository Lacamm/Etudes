package action;

import com.opensymphony.xwork2.ActionSupport;
import modele.CalculatriceDynamiqueDuFutur;
import modele.CalculatriceDynamiqueDuFuturImpl;

import java.util.Collection;

public class opeDynamique extends ActionSupport {

    CalculatriceDynamiqueDuFutur ope = new CalculatriceDynamiqueDuFuturImpl();
    public Collection<String> getOperateur() {;
        return ope.getOperations();
    }
}
