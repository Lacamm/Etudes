package action;

import com.opensymphony.xwork2.ActionSupport;

public class Saisie extends ActionSupport {

    String pseudo, pwd;

    public String getPseudo() {
        return pseudo;
    }

    public void setPseudo(String pseudo) {
        this.pseudo = pseudo;
    }

    public String getMotSecret() {
        return pwd;
    }

    public void setMotSecret(String pwd) {
        this.pwd = pwd;
    }

    @Override
    public String execute() throws Exception {
        if (this.pseudo.length() < 4) {
            addFieldError("pseudo", "Pseduo trop petit");
        }
        if (this.pwd.length() < 4) {
            addFieldError("motSecret", "Mot secret trop petit");
        }
        if (this.pwd.length() < 3 || this.pwd.length() < 3) {
            return "LengthError";
        }
        return SUCCESS;
    }
}
