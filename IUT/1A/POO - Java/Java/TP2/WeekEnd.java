import java.util.ArrayList;
public class WeekEnd{
   private ArrayList<Personne> listeAmis;
   private ArrayList<Depense> listeDepenses;

   public WeekEnd(){
       this.listeAmis = new ArrayList<Personne>();
       this.listeDepenses = new ArrayList<Depense>();
   }

   public void ajouterPersonne(Personne personne){this.listeAmis.add(personne);}
   public void ajouterDepense(Depense depense){this.listeDepenses.add(depense);}

   // totalDepensesPersonne prend paramètre une personne
   // et renvoie la somme des dépenses de cette personne.
   public double totalDepensesPersonne(Personne personne){
       return 1.2;
    }

   // totalDepenses renvoie la somme de toutes les dépenses.
   public double totalDepenses(){
       double total = 0.0;
       for(Depense produit:this.listeDepenses){
           total = total+produit.getMontant();
       }
        return total;
    }

   // depensesMoyenne renvoie la moyenne des dépenses par
   // personne
   public double depensesMoyenne(){return 1.4;}

   //depenseProduit prend un produit en paramètre et renvoie la
   // somme des dépenses pour ce produit.
   // (du pain peut avoir été acheté plusieurs fois...)
   public double depenseProduit(String produit){return 1.5;}

   // avoirPersonne prend en paramètre une personne et renvoie
   // son avoir pour le week end.
   public double avoirPersonne(Personne personne){return 1.6;}
}
