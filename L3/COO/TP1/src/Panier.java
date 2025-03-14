import java.util.ArrayList;


class Panier {
  private ArrayList<Corrige> achat = new ArrayList<Corrige>();
  private Paiement strat;

  private String nom;

  public Panier(String nom, Paiement strat) {
    this.nom = nom;
    this.strat = strat;
  }

  public float calculTotal() {
    float total = 0;
    for (int i=0; i<achat.size();i++){
      System.out.println("prix: "+achat.get(i).getPrix());
      total += achat.get(i).getPrix();
    }
    System.out.println("total = "+total);

    return total;
  }

  public void addAchat(Corrige c){
    achat.add(c);
  }

  public void paiement() {
    this.strat.paiement(calculTotal());
  }
}
