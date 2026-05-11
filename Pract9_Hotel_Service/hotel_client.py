import Pyro4

def main():

    ns = Pyro4.locateNS()

    uri = ns.lookup("hotel.booking")

    hotel = Pyro4.Proxy(uri)

    while True:

        print("\n===== HOTEL BOOKING SYSTEM =====")
        print("1. Book Room")
        print("2. Cancel Booking")
        print("3. View Bookings")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            guest = input("Enter guest name: ")

            result = hotel.book_room(guest)

            print(result)

        elif choice == "2":

            guest = input("Enter guest name: ")

            result = hotel.cancel_booking(guest)

            print(result)

        elif choice == "3":

            bookings = hotel.view_bookings()

            print("\nCurrent Bookings:")

            if bookings:
                for guest, status in bookings.items():
                    print(f"{guest} --> {status}")
            else:
                print("No bookings available.")

        elif choice == "4":

            print("Exiting Client...")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()