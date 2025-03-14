import java.util.Map;

public class Personnage extends PNJ {

  private Inventaire monInventaire;
  private int argent;

  public Personnage(String nom, int vie, int force, int intelligence, int defense)
  {
    super(nom,vie,force,intelligence,defense);
    Inventaire inventaire = new Inventaire(this);
    this.monInventaire = inventaire.InventaireDepart();
    this.argent = 10;
  }

  public Inventaire getMonInventaire() {
    return monInventaire;
  }

  public void setMonInventaire(Inventaire monInventaire) {
    this.monInventaire = monInventaire;
  }

  public void afficherInventaire(){
    monInventaire.afficherInventaire();
  }

  public void equiperObjet(String nom_objet) {monInventaire.equiper(nom_objet);}

  public void desequiperObjet(String nom_objet) {monInventaire.desequiper(nom_objet);}

  public void jeterObjet(String nom_objet) { monInventaire.jeterObjet(nom_objet);}

  public void consommerObjet(String nom_objet) {
    monInventaire.consommeObjet(nom_objet);
  }

  public void afficherStats()
  {
    System.out.println("========== Statistiques de " + this.getNom() + " ==========");
    System.out.println("Classe : " + this.getClasse());
    System.out.println("Vie : " + this.getVie() + "/" + this.getVieMax());
    System.out.println("Force : " + this.getForce());
    System.out.println("Intelligence : " + this.getIntelligence());
    System.out.println("Défense : " + this.getDefense());
    System.out.println("========================================" + "\n");
  }

  public void upgradeStats(Objet objet)
  {
    if(this.getVie() == this.getVieMax())
    {
      this.setVie(this.getVie() + objet.getPv());
      this.setVieMax(this.getVie());
    }
    else
      this.setVieMax(this.getVieMax() + objet.getPv());
    this.setForce(this.getForce() + objet.getAttaque());
    this.setDefense(this.getDefense() + objet.getDefense());
  }

  public void downgradeStats(Objet objet){
    if(objet.getPv() != 0)
    {
      this.setVie(this.getVie() - objet.getPv());
      this.setVieMax(this.getVie());
    }
    this.setForce(this.getForce() - objet.getAttaque());
    this.setDefense(this.getDefense() - objet.getDefense());
  }

  public int getArgent() {
    return argent;
  }

  public void setArgent(int argent) {
    this.argent = argent;
  }

  public void equiperObjetA(Objet objet) {monInventaire.equiperA(objet);}

  public void desequiperObjetA(Objet objet) {monInventaire.desequiperA(objet);}
}
