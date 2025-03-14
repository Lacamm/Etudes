
class PayPal implements Paiement {
  private String mail;

  private int numAutorisation;

  public PayPal(String mail, int numAutorisation) {
    this.mail = mail;
    this.numAutorisation = numAutorisation;
  }

  public void paiement(float montant){
    System.out.println("Paiement par PayPal de "+this.mail + " numéro : " + this.numAutorisation +
            ", avec un montant de " + montant + "€");
  }
}
