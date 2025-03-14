import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class Client {

    public static void main(String[] args) {

        String host = (args.length < 1) ? null : args[0];
        try {
            Registry registry = LocateRegistry.getRegistry(host);
            Sondage stub = (Sondage) registry.lookup("Sondage");

            stub.ajouterDate("01-02-2020");
            stub.ajouterDate("28-05-2000");
            stub.ajouterDate("02-04-2021");

            stub.ajouterVote("02-04-2021", 1);
            stub.ajouterVote("02-04-2021", 2);
            stub.ajouterVote("28-05-2000", 3);

            int rep = stub.nbVoixDate("28-05-2000");
            String reponse = stub.trouverDateChoisie();

            System.out.println("Date Choisie: " + reponse);
            System.out.println("Nombre votes pour 28-05-2000: " + rep);
        }
        catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}