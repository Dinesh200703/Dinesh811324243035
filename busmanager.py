import json
FILE_NAME="buses.json"
def load_buses():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except:
        return {}
def save_buses(buses):
    with open(FILE_NAME,"w") as f:
        json.dump(buses,f,indent=4)
while True:
    print("\n=== BUS MANAGER ===")
    print("1. Add Bus")
    print("2. View Buses")
    print("3. Exit")
    choice = int(input("Enter Choice: "))
    buses = load_buses()
    if choice==1:
        bus_name=input("Enter Bus Name: ")
        route=input("Enter Route: ")
        seats=int(input("Enter Total Seats: "))
        buses[bus_name]={
            "route": route,
            "seats": seats
        }
        save_buses(buses)
        print("Bus Added Successfully")
    elif choice==2:
        if not buses:
            print("No Buses Available")
        else:
            for name, details in buses.items():
                print("\nBus Name:",name)
                print("Route:",details["route"])
                print("Seats:",details["seats"])
    elif choice==3:
        break
    else:
        print("Invalid Choice")
