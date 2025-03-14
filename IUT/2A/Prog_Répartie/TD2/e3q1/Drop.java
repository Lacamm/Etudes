import java.util.*;

/*
    - sleep : le Thread s'endort mais ne libère pas l'objet
    Dans des blocs synchronized uniquement :
    - wait : le Thread libère l'objet et se met en état d'attente sur l'objet
    - notify : reveille un Thread en état d'attente sur l'objet
    - notifyAll : reveille tous les Threads en état d'attente sur cet objet
 */
public class Drop {

    private final List<String> messages = new ArrayList<>();
    private final static int n = 10;
    
    /*
    Prend un produit pour le consommer s'il est disponible.
    Sinon attend un produit.
     */
    public synchronized String take() {
        while (messages.size() == 0) {
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        String message = messages.get(0);
        messages.remove(0);
        notifyAll(); // pls consumer
        return message;
    }

    /*
    Ajoute un produit à la vente.
    Q1 (1 seul produit à la vente)
    Q3 (n produit à la vente)
     */
    public synchronized void put(String message) {
        while (messages.size() == n) {
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println("Message ajouté : "+message);
        messages.add(message);
        notifyAll(); // pls producer
    }
}
