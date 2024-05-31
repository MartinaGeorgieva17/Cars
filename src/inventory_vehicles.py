# inventory_vehicles.py

vehicles = []

def add_vehicle(): 
    create = input ("Create vehicle:" )
    model = input ("Enter vehicle model: ")
    year = input ("Enter vehicle year:")
    color = input ("Enter vehicle color:")
    mileage = input ('Enter vehicle mileage:')

    vehicle = {
        'number':len(vehicles)+1,
        'create': create, 
        'model':  model, 
        'year': year, 
        'color': color,
        'mileage': mileage
        }
    
    print('.'*50)

    vehicles.append(vehicle)
    print("Vehicle added to the inventory.")


    for count, vehicle in enumerate(vehicles, start=1):
        vehicle['number'] = count


def delete_vehicle():
    print("Deleting Vehicle from Your Inventory! ")
    vehicle_number = int(input("Enter the number of the vehicle you want to delete: "))

    found = False
    for vehicle in vehicles:
        if vehicle['number'] == vehicle_number:
            vehicles.remove(vehicle)
            print("Vehicle deleted from inventory.")
            found = True
            break

    if not found:
        print("Vehicle with the specified number does not exist.")

def view_inventory(): 
    print("Current Inventory: ")
    for count, vehicle in enumerate(vehicles, start=1):
        print(f"#{count}")
        print(f"Create: {vehicle['create']}")
        print(f"Model: {vehicle['model']}")
        print(f"Year: {vehicle['year']}")
        print(f"Color: {vehicle['color']}")
        print(f"Mileage: {vehicle['mileage']}")
        print('.'*50)  # Празен ред след всяко превозно средство

def update_vehicle():
    print("Updating Vehicle in Your Private Inventory!")
    vehicle_number = int(input("Enter the number of the vehicle you want to update: "))

    found = False
    for vehicle in vehicles:
        if vehicle['number'] == vehicle_number:
            print("Enter the new details for the vehicle:")
            create = input("Create new vehicle details: ")
            model = input("Enter new vehicle model: ")
            year = input("Enter new vehicle year: ")
            color = input("Enter new vehicle color: ")
            mileage = input("Enter new vehicle mileage: ")

            vehicle.update({
                'create': create,
                'model': model,
                'year': year,
                'color': color,
                'mileage': mileage
            })

            print("Vehicle details updated.")
            found = True
            break

    if not found:
        print("Vehicle with the specified number does not exist.")

def export_inventory(): 
    print("Exporting Current Inventory:")
    try:
        with open('inventory.txt', 'w') as file:
            for vehicle in vehicles:
                 file.write(f"{vehicle['number']}, {vehicle['create']}, {vehicle['model']}, {vehicle['year']}, {vehicle['color']}, {vehicle['mileage']}\n")
        print("Export successful!")
    except Exception as e:
        print(f"Error exporting inventory: {e}")