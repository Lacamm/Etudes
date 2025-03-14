
class Combat implements EtatJeu {

    public void gererEntreeDonjon(Contexte c, String nom) {
        System.out.println("Vous êtes déjà dans un donjon");
    }

    public void gererCreationPersonnage(Contexte c, String nom, FabriquePersonnage fabrique) {
        System.out.println("Vous ne pouvez pas créer de personnage en combat");
    }

    public void gererInventaire(Contexte c) {
        System.out.println("Vous ne pouvez pas afficher votre inventaire en combat");
    }

    public void gererBoutique(Contexte c) {
        System.out.println("Vous ne pouvez pas afficher la boutique, vous êtes en combat");
    }
    public void gererMenu(Contexte c){
        System.out.println("Vous ne pouvez pas voir le menu, vous êtes en combat");
    }

    public void gererSortieDonjon(Contexte c) {
        System.out.println("Vous ne pouvez pas sortir du donjon en plein combat");
    }

    public void gererAttaque(Contexte c, String nom) {
        if (c.getMonJeu().getPiece_courante().findEnnemis(nom)) {
            c.getMonJeu().attaquer(nom);
        } else {
            System.out.println("L'ennemi que vous voulez attaquer n'a pas été trouvé. Réessayer");
        }
        if (c.getMonJeu().getPiece_courante().getNbEnnemis() == 0) {
            System.out.println("Tous les ennemis sont morts, le combat est terminé");
            c.set_etat_courant(new InterieurDonjon());
        }
        if (c.getMonJeu().getPersonnage().getVie() <= 0) {
            c.getMonJeu().mortPerso();
            c.getMonJeu().afficherMenu();
            c.set_etat_courant(new Menu());
        }
    }

    public void gererEquiper(Contexte c, String nom_objet) {
        System.out.println("Vous ne pouvez pas équiper un objet, vous êtes en plein combat");
    }

    public void gererDesequiper(Contexte c, String nom_objet) {
        System.out.println("Vous ne pouvez pas désequiper un objet, vous êtes en plein combat");
    }

    public void gererConsommer(Contexte c, String nom_objet) {
        System.out.println("Vous ne pouvez pas consommer un objet, vous êtes en plein combat");
    }

    public void gererJeter(Contexte c, String nom_objet){
        System.out.println("Vous ne pouvez pas jeter d'objet, vous êtes en plein combat");
    }

    public void gererPieceSuivante(Contexte c) {
        System.out.println("Vous ne pouvez pas changer de pièce, vous êtes en plein combat");
    }

    public void gererAcheter(Contexte c, String nom_objet) {
        System.out.println("Vous ne pouvez pas acheter d'équipement, vous êtes en plein combat");
    }

    public void gererAmeliorer(Contexte c, String nom_objet) {
        System.out.println("Vous ne pouvez pas ameliorer votre équipement, vous êtes en plein combat");
    }

    public void gererEntrerMarchand(Contexte c){
        System.out.println("Vous ne pouvez pas entrer de chez le marchand, vous êtes en plein combat");
    }

    public void gererSortieMarchand(Contexte c){
        System.out.println("Vous ne pouvez pas sortir de chez le marchand, vous êtes en plein combat");
    }

}
