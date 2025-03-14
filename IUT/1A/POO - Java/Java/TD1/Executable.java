public class Executable {
 public static void main(String [] args) {
      Compte comp = new Compte("Durand", 25732);
      comp.crediter(2000);
      comp.debiter(7000);
      System.out.println(comp.getSolde());
  }
}