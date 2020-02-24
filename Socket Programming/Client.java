import java.io.*;
import java.lang.module.InvalidModuleDescriptorException;
import java.net.*;

public class Client {
    /*
     * Set socket, input and output streams
     */
    private Socket socket = null;
    private DataInputStream input = null;
    private DataOutputStream out = null;

    /*
     * !Creating a constructor for the IP adddress and port number
     */
    public Client(String address, int port) throws IOException {

        /*
         * ?Establish Connection with server
         */
        try {
            socket = new Socket(address, port);
            System.out.println("Connected with Server");

            /*
             * !Take input from client or user in terminal
             */
            input = new DataInputStream(System.in);

            // *Send output to the Socket for displaying in Server
            out = new DataOutputStream(socket.getOutputStream());

        } catch (UnknownHostException u) {
            System.out.println(u);
        }

        // !String to read message from input
        String line = "";

        // ! Keep reading until the input is "Over"
        while (!line.equals("Over")) {
            try {
                line = input.readLine();
                out.writeUTF(line);

            } catch (IOException i) {
                System.out.print(i);
            }

        }
        // ! Close the Connection
        try {
            input.close();
            out.close();
            socket.close();
        } catch (IOException i) {
            System.out.println(i);

        }
    }

    public static void main(String[] args) throws IOException {
        Client client = new Client("10.10.74.60", 1234);
    }

}