import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;


class Piece {
  private List<PNJ> listeEnnemis;
  private List<PNJ> listeVaincus;


  public Piece(){
    this.listeEnnemis = new ArrayList<>();
    this.listeVaincus = new ArrayList<>();
  }

  public void afficher_ennemis()
  {
    System.out.println("Voici les monstres présents : ");
    for(int i = 0; i < this.listeEnnemis.size(); i++)
    {
      System.out.println( this.listeEnnemis.get(i).getNom() + " le " + this.listeEnnemis.get(i).getClasse() + " | PV : " + this.listeEnnemis.get(i).getVie() + "/" + this.listeEnnemis.get(i).getVieMax());
    }
    System.out.println("");
  }

  public void add_ennemis(PNJ monstre)
  {
    this.listeEnnemis.add(monstre);
  }

  public PNJ getEnnemis(PNJ m)
  {
    for(PNJ monstre : this.listeEnnemis) {
      if (monstre.getNom() == m.getNom())
        return monstre;
    }
    return null;
  }

  public List<PNJ> getListeVaincus() {
    return listeVaincus;
  }

  public void save(){
    // Cette methode permet de remettre le donjon à son etat d'origine
    if(!this.listeEnnemis.isEmpty())
    {
      for(PNJ monstre : this.listeEnnemis)
      {
        monstre.setVie(monstre.getVieMax());
      }
    }
    for(PNJ monstre : this.listeVaincus)
    {
      if(!this.findEnnemis(monstre.getNom()))
        monstre.setVie(monstre.getVieMax());
        this.listeEnnemis.add(monstre);
    }
  }

  public void delEnnemis(PNJ monstre) {this.listeEnnemis.remove(monstre);}

  public List<PNJ> getListeEnnemis() {
    return listeEnnemis;
  }

  public PNJ getEnnemis(String nom) {
    for(PNJ monstre : this.listeEnnemis)
    {
      if(monstre.getNom().equals(nom))
        return monstre;
    }
    return null;
  }

  public boolean findEnnemis(String nom)
  {
    for(PNJ monstre : this.listeEnnemis)
    {
      if(monstre.getNom().equals(nom))
        return true;
    }
    return false;
  }

  public int getNbEnnemis(){ return this.listeEnnemis.size();}



}
