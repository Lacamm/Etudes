import java.util.*;

public class Serveur{

    private ArrayList<Client> listeClients;

    public Serveur() {
        this.listeClients = new ArrayList<Client>();
    }

    public void addClient(Client client) {
        this.listeClients.add(client);
    }

    public synchronized void sendto(String destinataire, String message) {
        for (Client c : this.listeClients) {
            if (c.getNom() == destinataire) {
                try {
                    if (c.getMessagerie().size() == 10) {
                        wait();
                        System.out.println("La boîte de " + c.getNom() + " est pleine");
                    }
                    else{
                        c.ajoutMessage(message);
                        System.out.println(c.getNom() + " a reçu un message");
                    }                    
                }
                catch (InterruptedException a) {}
            }
            notifyAll();
        }
    }

    public synchronized void recv(String user) {
        for (Client c : this.listeClients) {
            try {
                if (c.getNom() == user) {
                    if (c.getMessagerie().size() == 0) {
                        wait();
                        System.out.println("La messagerie de " + user + " est vide");
                    }
                    else {
                        System.out.println(user + " recupere le message " + c.getDernierMessage());
                        c.supprMessage(c.getDernierMessage());
                    }
                }
                Thread.sleep(5000);
            }
            catch (InterruptedException a) {}
            notifyAll();
        }
    }
}