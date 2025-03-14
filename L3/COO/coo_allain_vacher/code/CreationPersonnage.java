
class CreationPersonnage implements EtatJeu {

    public void gererEntreeDonjon(Contexte c, String nom){
        System.out.println("Vous ne pouvez pas entrer dans un donjon, vous n'avez même pas crée de personnage !");
    }

    public void gererCreationPersonnage(Contexte c,String nom, FabriquePersonnage fabrique){
        c.getMonJeu().creer_Personnage(nom,fabrique);
        c.getMonJeu().getPersonnage().afficherStats();
        c.getMonJeu().getPersonnage().afficherInventaire();
        c.getMonJeu().afficherMenu();
        c.set_etat_courant(new Menu());
    }
    public void gererInventaire(Contexte c){
        System.out.println("Vous ne pouvez pas voir votre inventaire, vous n'avez même pas crée de personnage !");
    }

    public void gererMenu(Contexte c){
        System.out.println("Vous ne pouvez pas voir le menu, vous n'avez même pas crée de personnage !");
    }

    public void gererBoutique(Contexte c)
    {
        System.out.println("Vous ne pouvez pas afficher la boutique, vous n'avez même pas crée de personnage !");
    }

    public void gererSortieDonjon(Contexte c){
        System.out.println("Vous ne pouvez pas sortir d'un donjon, vous n'avez même pas crée de personnage !");
    }

    public void gererEquiper(Contexte c, String nom_objet)
    {
        System.out.println("Vous ne pouvez pas equiper un objet, vous n'avez même pas crée de personnage !");
    }

    public void gererDesequiper(Contexte c, String nom_objet){
        System.out.println("Vous ne pouvez pas désequiper un objet, vous n'avez même pas de personnage !");
    }

    public void gererConsommer(Contexte c, String nom_objet){
        System.out.println("Vous ne pouvez pas consommer un objet, vous n'avez même pas de personnage !");
    }

    public void gererJeter(Contexte c, String nom_objet){
        System.out.println("Vous ne pouvez pas jeter d'objet, vous n'avez même pas crée de personnage !");
    }

    public void gererAttaque(Contexte c, String nom){
        System.out.println("Vous ne pouvez pas combattre, vous n'avez même pas crée de personnage !");
    }

    public void gererPieceSuivante(Contexte c) {
        System.out.println("Vous ne pouvez pas changer de pièce, vous n'êtes pas dans un donjon");
    }

    public void gererAcheter(Contexte c,String nom_objet) {
        System.out.println("Vous ne pouvez pas acheter d'équipement, vous n'avez même pas crée de personnage !");
    }

    public void gererAmeliorer(Contexte c, String nom_objet){
        System.out.println("Vous ne pouvez pas ameliorer votre équipement, vous n'avez même pas crée de personnage !");
    }

    public void gererEntrerMarchand(Contexte c){
        System.out.println("Vous ne pouvez pas entrer chez le marchand, vous n'avez même pas crée de personnage !");
    }

    public void gererSortieMarchand(Contexte c){
        System.out.println("Vous ne pouvez pas sortir de chez le marchand, vous n'avez même pas crée de personnage !");
    }
}
