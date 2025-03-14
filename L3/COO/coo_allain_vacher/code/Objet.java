
public class Objet{

  public static enum TYPE {TETE,BUSTE,JAMBES,PIEDS,ARME,CONSOMMABLE};

  private String nom;
  private Objet.TYPE type;
  private int pv;
  private int attaque;
  private int defense;
  private int poids;
  private int pvRendu;
  private String effet;
  private boolean ameliore;

  public Objet(String nom, Objet.TYPE type,int pv,int attaque, int defense, int poids, int pvRendu, String effet)
  {
    this.nom = nom;
    this.type = type;
    this.pv = pv;
    this.attaque = attaque;
    this.defense = defense;
    this.poids = poids;
    this.pvRendu = pvRendu;
    this.effet = effet;
    this.ameliore = false;
  }

  public Objet(){
    this.nom = "";
    this.type = null;
    this.pv = 0;
    this.attaque = 0;
    this.defense = 0;
    this.poids = 0;
    this.pvRendu = 0;
    this.effet = " ";
    this.ameliore = false;
  }

  public String getNom() {
    return nom;
  }

  public void setNom(String nom) {
    this.nom = nom;
  }

  public TYPE getType() {
    return type;
  }

  public void setType(TYPE type) {
    this.type = type;
  }

  public int getPv() {
    return pv;
  }

  public void setPv(int pv) {
    this.pv = pv;
  }

  public int getAttaque() {
    return attaque;
  }

  public void setAttaque(int attaque) {
    this.attaque = attaque;
  }

  public String getEffet() {
    return effet;
  }

  public void setEffet(String effet) {
    this.effet = effet;
  }

  public int getDefense() {
    return defense;
  }

  public void setDefense(int defense) {
    this.defense = defense;
  }

  public int getPoids() {
    return poids;
  }

  public void setPoids(int poids) {
    this.poids = poids;
  }

  public int getPvRendu() {
    return pvRendu;
  }

  public void setPvRendu(int pvRendu) {
    this.pvRendu = pvRendu;
  }

  public boolean isAmeliore() {
    return ameliore;
  }

  public void setAmeliore(boolean ameliore) {
    this.ameliore = ameliore;
  }
}
