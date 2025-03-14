public class Executable {

    public Executable(){};

    public static void main (String [] args){

        Corrige c1 = new Corrige((float)12.0,"fourchette");
        Corrige c2 = new Corrige((float)5.21,"alumette");
        Corrige c3 = new Corrige((float)78.145,"claquettes");

        Paiement cb = new CB(96314568, "bob");
        Paiement pp = new PayPal("truc@bidule.com", 1843375);

        Panier p1 = new Panier("PanierCB", cb);
        Panier p2 = new Panier("PanierPP", pp);


        p1.addAchat(c1);
        p1.paiement();
    }
}
