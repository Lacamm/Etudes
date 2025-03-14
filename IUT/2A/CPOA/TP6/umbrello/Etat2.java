
public class Etat2 {
  public Etat2 () {

    public void demarrer(Automate a){
      controle = a.getControle();
      controle.lancerChrono();
    }

    public void arreter(Automate a){
      a.arreterChrono();
    }

  }
}
