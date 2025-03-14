
class Boutique implements EtatJeu {

    public void gererEntreeDonjon(Contexte c,String nom){
        System.out.println("Vous ne pouvez pas entrer dans un donjon, vous êtes chez le marchand");
    }

    public void gererCreationPersonnage(Contexte c,String nom,FabriquePersonnage fabrique){
        System.out.println("Vous ne pouvez pas créer d'autres personnages");
    }

    public void gererInventaire(Contexte c){
        Personnage p = c.getMonJeu().getPersonnage();
        p.afficherStats();
        p.afficherInventaire();
    }

    public void gererBoutique(Contexte c)
    {
        c.getMonJeu().afficherBoutique();
    }

    public void gererMenu(Contexte c){
        System.out.println("Vous ne pouvez pas voir le menu, vous êtes dans la boutique du marchand");
    }

    public void gererSortieDonjon(Contexte c){
        System.out.println("Vous n'êtes même pas rentrer dans un donjon, vous ne pouvez donc pas en sortir");
    }

    public void gererAttaque(Contexte c, String nom){
        System.out.println("Vous ne pouvez pas combattre, vous n'êtes pas chez le marchand");
    }

    public void gererEquiper(Contexte c , String nom_objet)
    {
        c.getMonJeu().getPersonnage().equiperObjet(nom_objet);
    }

    public void gererDesequiper(Contexte c, String nom_objet){
        c.getMonJeu().desequiperObjet(nom_objet);
    }

    public void gererConsommer(Contexte c, String nom_objet){
        c.getMonJeu().consommerObjet(nom_objet);
    }

    public void gererJeter(Contexte c, String nom_objet){
        c.getMonJeu().jeterObjet(nom_objet);
    }

    public void gererPieceSuivante(Contexte c) {
        System.out.println("Vous ne pouvez pas changer de pièce, la boutique ne contient qu'une pièce");
    }

    public void gererAcheter(Contexte c,String nom_objet) {
        c.getMonJeu().acheter(nom_objet);
    }

    public void gererAmeliorer(Contexte c, String nom_objet){
        c.getMonJeu().ameliorer(nom_objet);
    }

    public void gererEntrerMarchand(Contexte c){
        System.out.println("Vous ne pouvez pas entrer  chez le marchand, vous y êtes déjà");
    }

    public void gererSortieMarchand(Contexte c){
        System.out.println(c.getMonJeu().getPersonnage_courant().getNom() + " décide de sortir de la boutique du marchand");
        c.set_etat_courant(new Menu());
    }

}
