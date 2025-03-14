
class Menu implements EtatJeu {

    public void gererEntreeDonjon(Contexte c,String nom){
        c.getMonJeu().entrerDonjon(nom);
        if( c.getMonJeu().getDonjon_courant() != null) {
            if (c.getMonJeu().getPiece_courante().getNbEnnemis() == 0)
            {
                c.set_etat_courant(new InterieurDonjon());
            }
            else {
                c.set_etat_courant(new Combat());
            }
        }
    }

    public void gererCreationPersonnage(Contexte c,String nom,FabriquePersonnage fabrique){
        System.out.println("Vous ne pouvez pas créer d'autres personnages");
    }

    public void gererInventaire(Contexte c){
        Personnage p = c.getMonJeu().getPersonnage();
        p.afficherStats();
        p.afficherInventaire();
    }

    public void gererMenu(Contexte c){
        c.getMonJeu().afficherMenu();
    }

    public void gererBoutique(Contexte c)
    {
        System.out.println("Vous ne pouvez pas voir la boutique, vous n'êtes pas chez le marchand");
    }

    public void gererSortieDonjon(Contexte c){
        System.out.println("Vous n'êtes même pas rentrer dans un donjon, vous ne pouvez donc pas en sortir");
    }

    public void gererAttaque(Contexte c, String nom){
        System.out.println("Vous ne pouvez pas combattre, vous n'êtes pas dans un donjon");
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
        System.out.println("Vous ne pouvez pas changer de pièce, vous n'êtes pas dans un donjon");
    }

    public void gererAcheter(Contexte c,String nom_objet) {
        System.out.println("Vous ne pouvez pas acheter un objet, vous n'êtes pas chez le marchand");
    }

    public void gererAmeliorer(Contexte c, String nom_objet){
        System.out.println("Vous ne pouvez pas améliorer votre objet, vous n'êtes pas chez le marchand");
    }

    public void gererEntrerMarchand(Contexte c){
        System.out.println(c.getMonJeu().getPersonnage_courant().getNom() + " décide d'aller voir le marchand dans sa boutique");
        c.set_etat_courant(new Boutique());
    }

    public void gererSortieMarchand(Contexte c){
        System.out.println("Vous ne pouvez pas sortir de chez le marchand, vous n'y êtes même pas entré");
    }



}
