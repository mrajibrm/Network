import java.rmi.*;
import java.rmi.server.*;

public class ServerRmi extends UnicastRemoteObject implements addRmi {
    public ServerRmi() throws RemoteException {

    }

    public static void main(String[] args) throws Exception {
        System.out.println("Server Starts.....");
        ServerRmi s = new ServerRmi();
        Naming.rebind("ServerRMI", s);

    }

    public int addNum(int a1, int a2) {
        return (a1 + a2);
    }
}