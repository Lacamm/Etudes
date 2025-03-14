public class Depense{
   private Personne personne;
   private double montant;
   private String produit;

   public Depense(Personne personne, double montant, String produit){
       this.personne = personne;
       this.montant = montant;
       this.produit = produit;
   }
   public double getMontant(){
       return this.montant;
   }
}