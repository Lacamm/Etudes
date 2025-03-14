
import java.util.*;

public class Bank {
  public Bank () { };
  
  public static void main(String[] args)
  {
    Client cl=new Client("Dupont");
      int rep=-1;
      Scanner sc=new Scanner(System.in);
      while(rep!=0){
          System.out.println("0. Quitter");
          System.out.println("1. Consulter un compte");
          System.out.println("2. Débiter un compte");
          System.out.println("3. Créditer un compte");
          System.out.println("4. Ajouter un compte");
          System.out.println("5. Consulter l'historique d'un compte");

          rep=sc.nextInt();
          sc.nextLine();

          switch(rep){
              case 1: {
                  System.out.print("Numéro du compte à Consulter : ");
                  String numero=sc.nextLine();
                  Compte co=cl.getCompte(numero);
                  System.out.println(co);break;
              }
              case 2: {
                  System.out.print("Numéro du compte à Débiter : ");
                  String numero=sc.nextLine();
                  Compte co=cl.getCompte(numero);
                  System.out.print("Montant du débit : ");
                  float montant=sc.nextFloat();
                  sc.nextLine();
                  co.debiter(montant,"débit");
                  break;
              }
              case 3: {
                  System.out.print("Numéro du compte à Créditer : ");
                  String numero=sc.nextLine();
                  Compte co=cl.getCompte(numero);
                  System.out.print("Montant du crédit : ");
                  float montant=sc.nextFloat();
                  sc.nextLine();
                  co.crediter(montant,"crédit");
                  break;
              }
              case 4: {
                  System.out.print("Compte (C)ourant ou de (D)épôt? ");
                  String s=sc.nextLine();
                  char c=s.charAt(0);
                  System.out.print("Numéro du compte à créer : ");
                  String numero=sc.nextLine();
                  Compte co;
                  if(c=='C') co=new CompteCourant(numero,0);
                  else co=new CompteDepot(numero,0);
                  cl.addComptes(co);
                  break;
              }
              case 5: {
                  System.out.print("Numéro du compte : ");
                  String numero=sc.nextLine();
                  Compte co=cl.getCompte(numero);
                  co.afficherHistorique();
                  break;
              }
            }
      }

  }


}
