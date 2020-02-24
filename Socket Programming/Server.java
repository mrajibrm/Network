import java.io.*;
import java.net.*;

public class Server {
    // Set socket and input stream
    private Socket socket = null;
    private ServerSocket server = null;
    private DataInputStream in = null;

    // Creating a constructor for initializing the port address
    public Server(int port) {
        // Server starts from here and wait for connection from client.
        try {
            server = new ServerSocket(port);
            System.out.println("Server Sttarted");
            System.out.println("Waiting for Client");
            socket = server.accept();
            System.out.println("Client accepted");

            // Get input from clint socket
            in = new DataInputStream(new BufferedInputStream(socket.getInputStream()));
            String line = "";

            // Timeout for reading the client side messages
            while (!line.equals("Over")) {
                try {
                    line = in.readUTF();
                    System.out.println(line);

                } catch (IOException i) {
                    System.out.print(i);

                }
            }
            System.out.println("Closing Connection");

            // Closing the connection
            socket.close();
            in.close();

        } catch (IOException i) {
            System.out.print(i);
        }
    }

    public static void main(String[] args) {
        Server server = new Server(1234);
    }
}