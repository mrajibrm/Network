import java.rmi.*;

//!Defining Remote Interface
interface addRmi extends Remote {
    public int addNum(int x, int y);
}