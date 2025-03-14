import java.rmi.Remote;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class Server {
    public static void main(String args[]) {
        try {
            SondImpl obj = new SondImpl();
            // objet exportable
            Remote stub= UnicastRemoteObject.exportObject(obj, 0);
            // Lie l'objet au registre
            Registry registry = LocateRegistry.getRegistry();
            registry.rebind("Sondage", stub);
            System.err.println("Server ready");
        }
        catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
