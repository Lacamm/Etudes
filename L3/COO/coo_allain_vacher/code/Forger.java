public class Forger extends Amelioration{

    private Objet objet;

    public Forger(Objet objet)
    {
        super(objet);
        objet.setAmeliore(true);
        objet.setEffet(objet.getEffet()+ " |  Boost : ");
        if(objet.getAttaque() != 0) {
            objet.setAttaque(objet.getAttaque() + 2);
            objet.setEffet(objet.getEffet()+ "Attaque +2 ");
        }
        if(objet.getDefense() != 0) {
            objet.setDefense(objet.getDefense() + 2);
            objet.setEffet(objet.getEffet()+ "Defense +2 ");
        }
        if(objet.getPv() != 0) {
            objet.setPv(objet.getPv() + 2);
            objet.setEffet(objet.getEffet()+ "PV +2 ");
        }
        this.objet = objet;
    }
}
