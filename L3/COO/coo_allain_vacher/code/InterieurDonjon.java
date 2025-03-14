
class InterieurDonjon implements EtatJeu {

    public void gererEntreeDonjon(Contexte c,String nom){
        System.out.println("Vous êtes déjà dans un donjon");
    }

    public void gererCreationPersonnage(Contexte c,String nom, FabriquePersonnage fabrique){
        System.out.println("Vous ne pouvez pas créer d'autres personnages");
    }

    public void gererInventaire(Contexte c){
        Personnage p = c.getMonJeu().getPersonnage();
        p.afficherStats();
        p.afficherInventaire();
    }

    public void gererBoutique(Contexte c)
    {
        System.out.println("Vous ne pouvez pas afficher la boutique, vous êtes dans un donjon");
    }

    public void gererMenu(Contexte c){
        System.out.println("Vous ne pouvez pas voir le menu, vvous êtes dans un donjon");
    }

    public void gererSortieDonjon(Contexte c){
        if(c.getMonJeu().getPiece_courante().getNbEnnemis() == 0) {
            c.getMonJeu().fuirDonjon();
            c.getMonJeu().afficherMenu();
            c.set_etat_courant(new Menu());
        }
        else
            System.out.println("Vous ne pouvez pas partir, il reste des ennemis vivants dans la salle");
    }

    public void gererAttaque(Contexte c, String nom){
        System.out.println("Le combat n'a pas encore debuté");
    }

    public void gererEquiper(Contexte c , String nom_objet)
    {
        c.getMonJeu().equiperObjet(nom_objet);
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

    public void gererPieceSuivante(Contexte c)
    {
        if( c.getMonJeu().getNombre_piece_courante() == c.getMonJeu().getDonjon_courant().getNbPiece() - 1) {
            c.getMonJeu().sortieDonjon();
            c.getMonJeu().afficherMenu();
            c.set_etat_courant(new Menu());
        }
        else {
            c.getMonJeu().pieceSuivante();
            if(c.getMonJeu().getPiece_courante().getNbEnnemis() == 0)
                c.set_etat_courant(new InterieurDonjon());
            else
                c.set_etat_courant(new Combat());
        }
    }

    public void gererAcheter(Contexte c,String nom_objet) {
        System.out.println("Vous ne pouvez pas acheter d'équipement, vous êtes dans un donjon");
    }

    public void gererAmeliorer(Contexte c, String nom_objet){
        System.out.println("Vous ne pouvez pas ameliorer votre équipement, vous êtes dans un donjon");
    }

    public void gererEntrerMarchand(Contexte c){
        System.out.println("Vous ne pouvez pas entrer de chez le marchand, vous êtes dans un donjon");
    }

    public void gererSortieMarchand(Contexte c){
        System.out.println("Vous ne pouvez pas sortir de chez le marchand, vous êtes dans un donjon");
    }



}
