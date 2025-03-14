
class CB implements Paiement {
  private int numCarte;

  private String nomClient;

  public CB(int numCarte, String nomClient) {
    this.numCarte = numCarte;
    this.nomClient = nomClient;
  }

  public void paiement(float montant){
      System.out.println("Paiement par carte de "+this.nomClient + " numéro de carte: " + this.numCarte +
              ", avec un montant de " + montant + "€");
  }
}
