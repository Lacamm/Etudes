package action;

import com.opensymphony.xwork2.ActionSupport;

import java.util.Arrays;
import java.util.Collection;

public class opeStatique extends ActionSupport {
    public Collection<String> getOperateur() {;
        return Arrays.asList(
                "Addition",
                "Soustraction",
                "Multiplication",
                "Division"
        );
    }
}
