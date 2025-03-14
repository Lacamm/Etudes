import java.util.Map;
import java.util.HashMap;

public class Marchand {

    private Map<Objet,Integer> boutique;
    private Map<Objet,Integer> stocks;

    public Marchand()
    {
        this.boutique = new HashMap<>();
        this.stocks = new HashMap<>();
    }

    public boolean findStock(String nom_objet)
    {
        for(Map.Entry<Objet,Integer> entree : this.stocks.entrySet())
        {
            if(entree.getKey().getNom().equals(nom_objet))
                return true;
        }
        return false;
    }

    public Objet getStock(String nom_objet)
    {
        for(Map.Entry<Objet,Integer> entree : this.stocks.entrySet())
        {
            if(entree.getKey().getNom().equals(nom_objet))
                return entree.getKey();
        }
        return null;
    }

    public boolean findBoutique(String nom_objet)
    {
        // Cette méthode permet de savoir si un objet est présent ou non dans l'inventaire
        for(Map.Entry<Objet,Integer> entree : this.boutique.entrySet())
        {
            if(entree.getKey().getNom().equals(nom_objet))
                return true;
        }
        return false;
    }

    public Objet getBoutique(String nom_objet)
    {
        // Cette méthode permet de savoir si un objet est présent ou non dans l'inventaire
        for(Map.Entry<Objet,Integer> entree : this.boutique.entrySet())
        {
            if(entree.getKey().getNom().equals(nom_objet))
                return entree.getKey();
        }
        return null;
    }

    public Objet achatObjet(String nom_objet)
    {
        if(this.findStock(nom_objet))
        {
            Objet objetStock = this.getStock(nom_objet);
            if(this.stocks.get(objetStock) == 1) {
                this.stocks.remove(objetStock);
            }
            else {
                this.stocks.put(objetStock, this.stocks.get(objetStock) - 1);
            }
            return objetStock;
        }
        else if(this.findBoutique(nom_objet))
        {
            Objet objetBoutique = this.getBoutique(nom_objet);
            if(!this.findStock(nom_objet))
            {
                this.boutique.remove(objetBoutique);
            }
            else{
                if(this.stocks.get(objetBoutique) == 1)
                    this.stocks.remove(objetBoutique);
                else {
                    this.stocks.put(objetBoutique, this.stocks.get(objetBoutique) - 1);
                }
            }
            return objetBoutique;
        }
        else
            return null;
    }

    public void addObjet(Objet objet,Integer prix)
    {
        if(this.boutique.containsKey(objet)){
            if(this.stocks.containsKey(objet)){
                this.stocks.put(objet,this.stocks.get(objet) + 1);
            }
            else {
                this.stocks.put(objet, 1);
            }
        }
        this.boutique.put(objet,prix);
    }

    public void acheter(Personnage perso,String nom_objet)
    {
        if(this.findBoutique(nom_objet)) {
            Objet achat = this.getBoutique(nom_objet);
            if (achat != null) {
                Integer prix = this.boutique.get(achat);
                if (prix <= perso.getArgent()) {
                    perso.setArgent(perso.getArgent() - prix);
                    System.out.println(perso.getNom() + " a acheté " + nom_objet + ".");
                    perso.getMonInventaire().ajouterObjet(achat);
                    this.achatObjet(nom_objet);
                } else
                    System.out.println("L'objet que vous souhaitez acheter est trop cher.");
            }
        }
        else
            System.out.println("Cet objet n'existe pas dans la boutique");
    }

    public void afficherBoutique()
    {
        System.out.println("Objets disponibles à l'achat : ");
        for(Map.Entry<Objet,Integer> entree : this.boutique.entrySet())
        {
            if(entree.getValue() < 10)
                System.out.println(  entree.getValue() + " $   |  " + entree.getKey().getNom() + " => " + entree.getKey().getEffet());
            else
                System.out.println(  entree.getValue() + " $  |  " + entree.getKey().getNom() + " => " + entree.getKey().getEffet());
        }
        System.out.println();
        System.out.println("Vous pouvez aussi améliorer un équipement pour 5 $.\n");
    }

    public void afficherStocks()
    {
        System.out.println("Objets dans les stocks : ");
        for(Map.Entry<Objet,Integer> entree : this.stocks.entrySet())
        {
            System.out.println( entree.getKey().getNom() + " : " + entree.getValue());
        }
        System.out.println();
    }
}
