import java.rmi.Remote;
import java.rmi.RemoteException;
import java.rmi.RemoteExcption;

//!Remote interface for the application
public interface Hello extends Remote {
    void printMsg() throws RemoteException;
}