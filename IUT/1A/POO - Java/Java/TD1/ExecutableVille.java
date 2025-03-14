public class Executable {
  public static void main(String [] args) {
      Ville ville = new Ville("Tours", "France");
      ville.setNbreHabitants(300756);
      System.out.println(ville.nbreHabitants());
  }
}

/*
1) On ajoute de nouveaux attributs et des nouvelles méthodes dans la classe.
 Dans l'éxecutable, il faut appeler ces nouvelles méthodes et modifier l'affichage.

2) Il faut connaître la superficie de la ville et le nombre d'habitants.
 Puis on crée une méthode qui calcule la densité.

*/