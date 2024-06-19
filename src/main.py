# 1. Вариант 1:

# import inventory_vehicles

# def main(): 
#     while True: 
#         print ('Auto Inventory!')
#         print('#1 Add Vehicle to Inventory')
#         print('#2 Delete Vehicle from Inventory')
#         print('#3 View Current Inventory')
#         print('#4 Update Vehicle in Inventory!')
#         print('#5 Export Current Inventory')
#         print('#6 Quit')

#         print('.' *50)
#         choice = input('Please, choose from one of the above option:')
#         print('.' *50)

#         if choice == '1':
#             inventory_vehicles.add_vehicle()
#         elif choice == '2':
#             inventory_vehicles.delete_vehicle()
#         elif choice == '3':
#             inventory_vehicles.view_inventory()
#         elif choice =='4':
#             inventory_vehicles.update_vehicle()
#         elif choice == '5':
#             inventory_vehicles.export_inventory()
#         elif choice == '6':
#             print('Thanks for using the programme!')
#             break
#         else: 
#             print('Invalid choice. Please, try again! ')

# if __name__ == "__main__":
#     main() 



# Вариант 2: с класове: 

from inventory_vehicles import Inventory

def main():
    inventory = Inventory()
    
    while True:
        print('Auto Inventory!')
        print('#1 Add Vehicle to Inventory')
        print('#2 Delete Vehicle from Inventory')
        print('#3 View Current Inventory')
        print('#4 Update Vehicle in Inventory!')
        print('#5 Export Current Inventory')
        print('#6 Quit')

        print('.' * 50)
        choice = input('Please, choose from one of the above options:')
        print('.' * 50)

        if choice == '1':
            inventory.add_vehicle()
        elif choice == '2':
            inventory.delete_vehicle()
        elif choice == '3':
            inventory.view_inventory()
        elif choice == '4':
            inventory.update_inventory()
        elif choice == '5':
            inventory.export_inventory()
        elif choice == '6':
            print('Thanks for using the program!')
            break
        else:
            print('Invalid choice. Please, try again!')

if __name__ == "__main__":
    main()



