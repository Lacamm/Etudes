import java.util.Random;

public abstract class PNJ {

  private String nom;
  private int vie;
  private int force;
  private int intelligence;
  private int defense;
  private int vieMax;
  private String classe;

  public PNJ(String nom,int vie,int force, int intelligence, int defense){
    this.nom = nom;
    this.vie = vie;
    this.force = force;
    this.intelligence = intelligence;
    this.defense = defense;
    this.vieMax = vie;
    this.classe = String.valueOf(this.getClass()).replace("class ","");
  }

  public String getNom() {
    return nom;
  }

  public int getForce() {
    return force;
  }

  public int getIntelligence() {
    return intelligence;
  }

  public int getDefense() {
    return defense;
  }

  public int getVie() {
    return vie;
  }

  public int getVieMax() {
    return vieMax;
  }

  public void setVieMax(int vieMax) {
    this.vieMax = vieMax;
  }

  public void setNom(String nom) {
    this.nom = nom;
  }

  public void setForce(int force) {
    this.force = force;
  }

  public void setIntelligence(int intelligence) {
    this.intelligence = intelligence;
  }

  public void setDefense(int defense) {
    this.defense = defense;
  }

  public void setVie(int vie) {
    this.vie = vie;
  }

  public String getClasse() {
    return classe;
  }

  public void setClasse(String classe) {
    this.classe = classe;
  }

  public void attaquer(PNJ adversaire) {
    int degats = this.getForce() - adversaire.getDefense();
    double chance_crit = 5 * this.getIntelligence();
    int tirage_crit = 0;
    Random random = new Random();
    tirage_crit = random.nextInt(101);
    if (degats > 0) {
      if(tirage_crit <= chance_crit ) {
        if(degats == 1)
          degats = 2;
        else
          degats = (int)(degats * 1.4);
        System.out.println(this.getNom() + " a attaqué " + adversaire.getNom() + " et lui inflige un coup critique de " + degats + " point(s) de dégats.");
      }
      else
        System.out.println(this.getNom() + " a attaqué " + adversaire.getNom() + " et lui inflige " + degats + " point(s) de dégats.");
      adversaire.setVie(adversaire.getVie() - degats);
    } else
      System.out.println("L'attaque de " + this.getNom() + " n'a pas fait de dégats");
    if(adversaire.getVie() <= 0)
    {
      System.out.println(adversaire.getNom() + " est mort de la main de " + this.getNom());
    }
  }

  public void boss()
  {
    this.setVie((int) (this.getVie() * 1.2));
    this.setVieMax(this.getVie());
    this.setDefense((int) (this.getDefense() * 1.2));
    this.setForce((int) (this.getForce() * 1.2));
    this.setIntelligence((int) (this.getIntelligence() * 1.2));
    this.setClasse(this.getClasse() + " (Boss)");
  }

}
