import java.rmi.RemoteException;

public class CalcImpl implements Calculatrice {
    @Override
    public int somme(int a, int b) throws RemoteException {
        return a+b;
    }

    @Override
    public int soustraction(int a, int b) throws RemoteException {
        return a-b;
    }

    @Override
    public int multiplication(int a, int b) throws RemoteException {
        return a*b;
    }

    @Override
    public int division(int a, int b) throws RemoteException {
        return a/b;
    }
}
