import json
from abc import ABC, abstractmethod
FILE_NAME = "buses.json"
class Ticket:
    def __init__(self, ticket_id, passenger_name, bus_name,
                 seat_number, source, destination):
        self.__ticket_id = ticket_id
        self.__passenger_name = passenger_name
        self.__bus_name = bus_name
        self.__seat_number = seat_number
        self.__source = source
        self.__destination = destination
    @property
    def ticket_id(self):
        return self.__ticket_id
    @property
    def passenger_name(self):
        return self.__passenger_name
    @property
    def bus_name(self):
        return self.__bus_name
    @property
    def seat_number(self):
        return self.__seat_number
    @property
    def source(self):
        return self.__source
    @property
    def destination(self):
        return self.__destination
class ReservationSystem(ABC):
    @abstractmethod
    def show_buses(self):
        pass
    @abstractmethod
    def book_ticket(self):
        pass
    @abstractmethod
    def view_ticket(self):
        pass
class BusReservation(ReservationSystem):
    def __init__(self):
        try:
            with open(FILE_NAME, "r") as f:
                self.buses = json.load(f)
        except:
            self.buses = {}
        self.booked_tickets = {}
        self.ticket_id = 1001
    def show_buses(self):
        if not self.buses:
            print("No Buses Available")
            return
        print("\n========== AVAILABLE BUSES ==========")
        for bus_name, details in self.buses.items():
            booked = sum(
                1
                for ticket in self.booked_tickets.values()
                if ticket.bus_name == bus_name
            )
            available = details["seats"] - booked
            print("\nBus Name :", bus_name)
            print("Route :", details["route"])
            print("Total Seats :", details["seats"])
            print("Available Seats :", available)
            print("-" * 35)
    def book_ticket(self):
        if not self.buses:
            print("No Buses Available")
            return
        self.show_buses()
        bus_name = input("\nEnter Bus Name : ")
        if bus_name not in self.buses:
            print("Invalid Bus Name")
            return
        booked_seats = [
            ticket.seat_number
            for ticket in self.booked_tickets.values()
            if ticket.bus_name == bus_name
        ]
        print("\nAvailable Seats :")
        for seat in range(1, self.buses[bus_name]["seats"] + 1):
            if seat not in booked_seats:
                print(seat, end=" ")
        print()
        seat_number = int(input("\nEnter Seat Number : "))
        if seat_number < 1 or seat_number > self.buses[bus_name]["seats"]:
            print("Invalid Seat Number")
            return
        if seat_number in booked_seats:
            print("Seat Already Booked")
            return
        passenger_name = input("Enter Passenger Name : ")
        source = input("Enter Source : ")
        destination = input("Enter Destination : ")
        ticket = Ticket(
            self.ticket_id,
            passenger_name,
            bus_name,
            seat_number,
            source,
            destination
        )
        self.booked_tickets[self.ticket_id] = ticket
        print("\nTicket Booked Successfully")
        print("Ticket ID :", self.ticket_id)
        self.ticket_id += 1
    def view_ticket(self):
        ticket_id = int(input("Enter Ticket ID : "))
        if ticket_id not in self.booked_tickets:
            print("Ticket Not Found")
            return
        ticket = self.booked_tickets[ticket_id]
        print("\n========== TICKET DETAILS ==========")
        print("Ticket ID :", ticket.ticket_id)
        print("Passenger Name :", ticket.passenger_name)
        print("Bus Name :", ticket.bus_name)
        print("Seat Number :", ticket.seat_number)
        print("Source :", ticket.source)
        print("Destination :", ticket.destination)
class PremiumBusReservation(BusReservation):
    def book_ticket(self):
        print("\n*** Premium Bus Booking ***")
        super().book_ticket()
reservation = PremiumBusReservation()
while True:
    print("\n========== BUS RESERVATION SYSTEM ==========")
    print("1. View Available Buses")
    print("2. Book Ticket")
    print("3. View Ticket")
    print("4. Exit")
    choice = int(input("Enter Choice : "))
    if choice == 1:
        reservation.show_buses()
    elif choice == 2:
        reservation.book_ticket()
    elif choice == 3:
        reservation.view_ticket()
    elif choice == 4:
        print("Thank You")
        break
    else:
        print("Invalid Choice")
