import Pyro4

#python -m Pyro4.naming

@Pyro4.expose
class HotelBookingSystem:

    def __init__(self):
        self.bookings = {}

    # Book room
    def book_room(self, guest_name):

        if guest_name in self.bookings:
            return f"Room already booked for {guest_name}"

        self.bookings[guest_name] = "Booked"

        return f"Room booked successfully for {guest_name}"

    # Cancel booking
    def cancel_booking(self, guest_name):

        if guest_name not in self.bookings:
            return f"No booking found for {guest_name}"

        del self.bookings[guest_name]

        return f"Booking cancelled for {guest_name}"

    # View all bookings
    def view_bookings(self):
        return self.bookings


def main():

    daemon = Pyro4.Daemon()

    ns = Pyro4.locateNS()

    hotel = HotelBookingSystem()

    uri = daemon.register(hotel)

    ns.register("hotel.booking", uri)

    print("Hotel Booking Server is Running...")
    print("URI:", uri)

    daemon.requestLoop()


if __name__ == "__main__":
    main()