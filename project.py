flights = [
    ["F501", "Mumbai", "Delhi", 40],
    ["F235", "Delhi", "Bengaluru", 35],
    ["F675", "Chennai", "Kolkata", 25],
    ["F543", "Hyderabad", "Pune", 20],
    ["F765", "Ahmedabad", "Jaipur", 30],
    ["F897", "Goa", "Chandigarh", 15]
]

bookings = []

def show_flights():
    print("\nAvailable Flights:")
    for f in flights:
        print("Flight:", f[0], "| From:", f[1], "| To:", f[2], "| Seats Left:", f[3])

def get_flght_by_id(flight_id):
    for f in flights:
        if f[0] == flight_id:
            return f
    return None

def print_ticket(name, flight):
    print("\nTicket")
    print("Passenger:", name)
    print("Flight ID:", flight[0])
    print("From:", flight[1])
    print("To:", flight[2])

def book_flight():
    show_flights()

    flight_id = input("Enter the Flight ID for the outbound journey: ")
    flight = get_flght_by_id(flight_id)

    if not flight:
        print("Flight not found")
        return
    
    if flight[3] <= 0:
        print("No seats left on this flight")
        return

    name = input("Enter your name: ")

    print("\nDo you want a return ticket")
    print("1. Yes")
    print("2. No")
    rt_choice = input("Enter your choice: ")

    
    flight[3] -= 1
    bookings.append([name, flight_id])
    print("\nOutbound ticket booked")
    print_ticket(name, flight)

    
    if rt_choice == "1":
        show_flights()
        return_id = input("Enter the Flight ID for the return journey: ")
        return_flight = get_flght_by_id(return_id)

        if not return_flight:
            print("Return flight not found")
            return
        
        if return_flight[3] <= 0:
            print("No seats left on the return flight")
            return

        
        return_flight[3] -= 1
        bookings.append([name, return_id])
        print("Return ticket booked")
        print_ticket(name, return_flight)

def view_bookings():
    if len(bookings) == 0:
        print("\nNo bookings yet")
    else:
        print("\nAll Bookings:")
        for b in bookings:
            print("Passenger:", b[0], "| Flight:", b[1])

def main():
    while True:
        print("\nFlight Booking System")
        print("1. View Flights")
        print("2. Book a Flight")
        print("3. View All Bookings")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_flights()
        elif choice == "2":
            book_flight()
        elif choice == "3":
            view_bookings()
        elif choice == "4":
            print("Thank you for using the Flight Booking System")
            break
        else:
            print("Invalid choice, try again")

main()