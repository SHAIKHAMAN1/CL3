import java.rmi.Remote;
import java.rmi.RemoteException;

public interface HotelServiceInterface extends Remote {

    String bookRoom(String guestName) throws RemoteException;

    String cancelBooking(String guestName) throws RemoteException;

    String viewBookings() throws RemoteException;
}