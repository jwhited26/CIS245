#Build Vehicle class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def set_vehicle_make(self, make):
        self.make = make

    def set_vehicle_model(self, model):
        self.model = model

    def get_vehicle_make(self):
        return self.make

    def get_vehicle_model(self):
        return self.model

#Build Car Class
class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def set_car_doors(self, doors):
        self.doors = doors

    def get_car_doors(self):
        return self.doors

#Build Pickup Class
class Pickup(Vehicle):
    def __init__(self, make, model, bed_length):
        super().__init__(make, model)
        self.bed_length = bed_length

    def set_bed_length(self, bed_length):
        self.bed_length = bed_length

    def get_bed_length(self):
        return self.bed_length

garage = []

#Prompt user to add vehicles or quit
while True:
    print("Enter 1 to add a car, 2 to add a truck,")
    print("3 to list your vehicles, or 4 to quit:")
    option = int(input("Enter your option: "))

    if option == 1:
        make = input("Enter car make: ")
        model = input("Enter car model: ")
        doors = int(input("Enter number of doors: "))
        car = Car(make, model, doors)
        garage.append(car)
    elif option == 2:
        make = input("Enter truck make: ")
        model = input("Enter truck model: ")
        bed_length = float(input("Enter bed length: "))
        pickup = Pickup(make, model, bed_length)
        garage.append(pickup)
    elif option == 3:
        for i, vehicle in enumerate(garage):
            print(f"Vehicle {i + 1}: {vehicle.get_vehicle_make()} {vehicle.get_vehicle_model()}")
            if isinstance(vehicle, Car):
                print(f"Doors: {vehicle.get_car_doors()}")
            elif isinstance(vehicle, Pickup):
                print(f"Bed Length: {vehicle.get_bed_length()}")
    elif option == 4:
        break
    else:
        print("Invalid option, try again.")