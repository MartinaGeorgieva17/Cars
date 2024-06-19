# inventory_vehicles.py
# Вариант 1
# vehicles = []

# def add_vehicle(): 
#     create = input ("Create vehicle:" )
#     model = input ("Enter vehicle model: ")
#     year = input ("Enter vehicle year:")
#     color = input ("Enter vehicle color:")
#     mileage = input ('Enter vehicle mileage:')

#     vehicle = {
#         'number':len(vehicles)+1,
#         'create': create, 
#         'model':  model, 
#         'year': year, 
#         'color': color,
#         'mileage': mileage
#         }
    
#     print('.'*50)

#     vehicles.append(vehicle)
#     print("Vehicle added to the inventory.")


#     for count, vehicle in enumerate(vehicles, start=1):
#         vehicle['number'] = count


# def delete_vehicle():
#     print("Deleting Vehicle from Your Inventory! ")
#     vehicle_number = int(input("Enter the number of the vehicle you want to delete: "))

#     found = False
#     for vehicle in vehicles:
#         if vehicle['number'] == vehicle_number:
#             vehicles.remove(vehicle)
#             print("Vehicle deleted from inventory.")
#             found = True
#             break

#     if not found:
#         print("Vehicle with the specified number does not exist.")

# def view_inventory(): 
#     print("Current Inventory: ")
#     for count, vehicle in enumerate(vehicles, start=1):
#         print(f"#{count}")
#         print(f"Create: {vehicle['create']}")
#         print(f"Model: {vehicle['model']}")
#         print(f"Year: {vehicle['year']}")
#         print(f"Color: {vehicle['color']}")
#         print(f"Mileage: {vehicle['mileage']}")
#         print('.'*50)  # Празен ред след всяко превозно средство

# def update_vehicle():
#     print("Updating Vehicle in Your Private Inventory!")
#     vehicle_number = int(input("Enter the number of the vehicle you want to update: "))

#     found = False
#     for vehicle in vehicles:
#         if vehicle['number'] == vehicle_number:
#             print("Enter the new details for the vehicle:")
#             create = input("Create new vehicle details: ")
#             model = input("Enter new vehicle model: ")
#             year = input("Enter new vehicle year: ")
#             color = input("Enter new vehicle color: ")
#             mileage = input("Enter new vehicle mileage: ")

#             vehicle.update({
#                 'create': create,
#                 'model': model,
#                 'year': year,
#                 'color': color,
#                 'mileage': mileage
#             })

#             print("Vehicle details updated.")
#             found = True
#             break

#     if not found:
#         print("Vehicle with the specified number does not exist.")

# def export_inventory(): 
#     print("Exporting Current Inventory:")
#     try:
#         with open('inventory.txt', 'w') as file:
#             for vehicle in vehicles:
#                  file.write(f"{vehicle['number']}, {vehicle['create']}, {vehicle['model']}, {vehicle['year']}, {vehicle['color']}, {vehicle['mileage']}\n")
#         print("Export successful!")
#     except Exception as e:
#         print(f"Error exporting inventory: {e}")



# Вариант 2 с класове: 

class Vehicle: 
    def __init__ (self, create, model, year, color, mileage):
        self.create = create
        self. model = model 
        self. year = year
        self.color = color 
        self.mileage = mileage

    def __str__(self):
        return f"{self.create}, {self.model}, {self.year}, {self.color}, {self.mileage}"
    

class Inventory:
    def __init__(self):
        self.vehicles =[]

    def add_vehicle(self):
        create = input ('Create vehicle:')
        model = input ("Enter vehicle model:")
        year = input ("Enter vehicle year:")
        color = input ('Enter vehicle color: ')
        mileage = input ('Enter vehicle mileage')

        vehicle = Vehicle (create, model, year, color, mileage)
        self.vehicles.append(vehicle)
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
        for count, vehicle in enumerate(self, vehicle, start=1):
            print(f"#{count}'):{vehicle}")
            print('.'*50)

    def update_inventory(self):
        print("Uprdating vehicle in your inventory.")
        vehicle_number = int(input('Enter the number of the vehicle you want to update:'))

        if 0<vehicle_number<=len(self.vehicles):
            vehicle = self.vehicles[vehicle_number-1]
            print ('Enter the new details for the vehicle:')

            vehicle.create=input ("Create new vehicle details:")
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
                    file.write(f"{count}, {vehicle.create}, {vehicle.model}, {vehicle.year}, {vehicle.color}, {vehicle.mileage}\n")
                    print("Export Successful!")
        except Exception as e:
            print (f"Error exporting inventory {e}")           





        
