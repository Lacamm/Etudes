class Compte{
    // varibles
    private String nom = this.nom;
    private int solde = this.solde;    
    
    // constructeur
    public void Compte(Sting nom, int solde){
        this.nom, this.solde;
    }

    // getter
    public int getSolde(){return this.solde;}

    // setters
    public void crediter(int entree){this.solde+entree;}
    public void debiter(int sortie){this.solde-sortie;}

}