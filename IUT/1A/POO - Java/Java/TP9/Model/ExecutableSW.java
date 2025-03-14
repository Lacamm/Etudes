public class ExecutableSW{
  public static void main(String[] args) {
    Personnage p1=new Ewok("Wicket",false,20,"bleu");
    System.out.println(p1);
    // Doit afficher :
    // Je suis un Ewok, je m'appelle Wicket, je suis un garçon,
    // j'ai 20 points de vie et je porte un chapeau bleu

    Personnage p2=new Wookie("Chewbaka",false,56,4);
    System.out.println(p2);
    // Doit afficher :
    // Je suis un Wookie, je m'appelle Chewbaka, je suis un garçon,
    // j'ai 56 points de vie et j'ai 4 enfants

    Personnage p3=new Jedi("Alora",true,45);
    System.out.println(p3);
    // Doit afficher :
    // Je suis un Jedi, je m'appelle Alora, je suis une fille,
    // j'ai 45 points de vie

    p2.attaque(p3,6); // p2 enlève 6 points de vie à p3
    System.out.println(p3);
    // Doit afficher :
    // Je suis un Jedi, je m'appelle Alora, je suis une fille,
    // j'ai 39 points de vie
    }
}