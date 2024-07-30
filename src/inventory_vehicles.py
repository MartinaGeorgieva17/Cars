from db.operations import MySQLDB

class Vehicle:
    def __init__ (self, manufacturer, model, year, color, mileage):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage


class Inventory:
    def __init__(self):
        self.vehicles =[]
        self.db = MySQLDB()

    def add_vehicle(self):
        manufacturer = input ('Enter manufacturer:')
        model = input ("Enter vehicle model:")
        year = input ("Enter vehicle year:")
        color = input ('Enter vehicle color: ')
        mileage = input ('Enter vehicle mileage')

        vehicle = Vehicle(manufacturer, model, year, color, mileage)
        self.vehicles.append(vehicle)
        self.db.add_vehicle(vehicle)

        print("Vehicle added to your inventory.")

    def delete_vehicle(self):
        print("Deleting vehicle from your inventory.")
        vehicle_number = int(input("Enter the number of the vehicle you want to delete:"))
        if 0 < vehicle_number <= len(self.vehicles):
            del self.vehicles[vehicle_number -1]
            print("Vehicle deleted from the inventory.")
        else:
            print('Vehicle does not exist. Try with valid number.')
    def view_inventory(self):
        print("Current Inventory:")
        for count, vehicle in enumerate(self.vehicles, start=1):
            print(f"#{count}'): {vehicle}")
            print('.'*50)
    def update_inventory(self):
        print("Uprdating vehicle in your inventory.")
        vehicle_number = int(input('Enter the number of the vehicle you want to update:'))
        if 0<vehicle_number<=len(self.vehicles):
            vehicle = self.vehicles[vehicle_number-1]
            print ('Enter the new details for the vehicle:')
            vehicle.model = input ("Enter vehicle model: ")
            vehicle.year = input ("Crete new year for the vehicle: ")
            vehicle.color = input ('Create new color for the vehicle: ')
            vehicle.mileage = input ("Create new mileage for the vehicle: ")
            print("Vehicle details updated!")
        else:
            print('Vehicle with specific number does not exist!')
    def export_inventory(self):
        print("Exporting Current Inventory.")
        try:
            with open ('Inventory.txt', 'w') as file:
                for count, vehicle in enumerate(self.vehicles, start = 1):
                    file.write(f"{count}, {vehicle.manufacturer}, {vehicle.model}, {vehicle.year}, {vehicle.color}, {vehicle.mileage}\n")
                    print("Export Successful!")
        except Exception as e:
            print (f"Error exporting inventory {e}")

    


  




