import java.util.*;
import java.util.Random;

public class Client extends Thread{

    private String nom;
    private ArrayList<String> messagerie;

    public Serveur serveur;

    private final Random r = new Random();

    private final static String[] contacts = {
        "Pierre",
        "Paul",
        "Jacques"
    };

    private final static String[] sms = {
        "blabla",
        "toto",
        "truc"
    };

    public Client(String nom, Serveur serveur){
        this.nom = nom;
        this.messagerie = new ArrayList<String>();

        this.serveur = serveur;
        serveur.addClient(this);
    }

    public void run(){
        try{
            while(true){
                String destinataire = contacts[r.nextInt(contacts.length)];
                String texte = sms[r.nextInt(sms.length)];
                serveur.sendto(destinataire, texte);
                try{                    
                    Thread.sleep(200);
                }
                catch(Exception e){e.printStackTrace();}	

                System.out.println("Message envoyé");

                String expediteur = contacts[r.nextInt(contacts.length)];
                serveur.recv(expediteur);
                try{                    
                    Thread.sleep(200);
                }
                catch(Exception e){e.printStackTrace();}	

                System.out.println("Message reçu");

            }
        }
        catch(Exception e){e.printStackTrace();}
    }

    public String getNom(){
        return this.nom;
    }

    public void ajoutMessage(String message){
        this.messagerie.add(message);
    }

    public ArrayList<String> getMessagerie(){
        return this.messagerie;
    }

    public String getDernierMessage(){
        return this.messagerie.get(this.messagerie.size()-1);
    }

    public void supprMessage(String message){
        this.messagerie.remove(message);
    }
}