class Flight:
    def __init__(self, code, source, destination, fare, seats):
        self.code = code
        self.source = source
        self.destination = destination
        self.fare = fare
        self.seats = seats


class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def discount(self):
        return 0


class Student(Passenger):
    def discount(self):
        return 0.10


class Booking:
    def __init__(self, flight, passenger, tickets):
        self.flight = flight
        self.passenger = passenger
        self.tickets = tickets

    def show(self):
        total = self.flight.fare * self.tickets
        total -= total * self.passenger.discount()
        print("Passenger:", self.passenger.name)
        print("Flight:", self.flight.code)
        print("Tickets:", self.tickets)
        print("Total Fare: Rs.", total)


flights = [
    Flight("PN101", "Pune", "Delhi", 4000, 20),
    Flight("MB202", "Mumbai", "Bengaluru", 3500, 15),
    Flight("PN303", "Pune", "Hyderabad", 3000, 18)
]

print("1. View Flights")
print("2. Book Flight")
choice = input("Enter choice: ")

if choice == "1":
    for f in flights:
        print(f.code, f.source, "to", f.destination, f.fare)

elif choice == "2":
    code = input("Flight code: ")
    flight = next((f for f in flights if f.code == code), None)

    if flight:
        name = input("Passenger name: ").strip()
        try:
            age = int(input("Age: "))
            tickets = int(input("Tickets: "))

            if not name or age <= 0 or tickets <= 0 or tickets > flight.seats:
                print("Invalid booking details!")
            else:
                kind = input("Student or Regular: ").lower()
                if kind == "student":
                    passenger = Student(name, age)
                elif kind == "regular":
                    passenger = Passenger(name, age)
                else:
                    print("Invalid passenger type!")
                    passenger = None

                if passenger:
                    flight.seats -= tickets
                    booking = Booking(flight, passenger, tickets)
                    booking.show()
        except ValueError:
            print("Enter valid numbers!")
    else:
        print("Flight not found!")
else:
    print("Invalid choice!")