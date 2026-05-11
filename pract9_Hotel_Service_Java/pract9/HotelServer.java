import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;

public class HotelServer extends UnicastRemoteObject implements HotelServiceInterface {

    // Stores booking information
    private HashMap<String, String> bookings = new HashMap<>();

    // Constructor
    protected HotelServer() throws RemoteException {
        super();
    }

    // Book a room
    @Override
    public String bookRoom(String guestName) throws RemoteException {

        if (bookings.containsKey(guestName)) {
            return "Room already booked for: " + guestName;
        }

        bookings.put(guestName, "Room Booked");

        return "Room successfully booked for: " + guestName;
    }

    // Cancel booking
    @Override
    public String cancelBooking(String guestName) throws RemoteException {

        if (!bookings.containsKey(guestName)) {
            return "No booking found for: " + guestName;
        }

        bookings.remove(guestName);

        return "Booking cancelled for: " + guestName;
    }

    // View all bookings
    @Override
    public String viewBookings() throws RemoteException {

        if (bookings.isEmpty()) {
            return "No current bookings.";
        }

        return "Current Bookings: " + bookings.keySet().toString();
    }

    // Main method
    public static void main(String[] args) {

        try {

            // Create server object
            HotelServer server = new HotelServer();

            // Create RMI registry on port 6000
            Registry registry = LocateRegistry.createRegistry(6001);

            // Bind server object with name
            registry.rebind("HotelService", server);

            System.out.println("Hotel Server is running and ready...");

        } catch (Exception e) {

            System.out.println("Server Error: " + e.getMessage());
        }
    }
}