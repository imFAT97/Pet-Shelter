# main.py
from termcolor import colored
from pet_shelter import PetShelter
from utils import add_pet_from_input, display_menu, update_pet, delete_pet, save_to_file, load_from_file

if __name__ == "__main__":
    shelter = PetShelter()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            pet = add_pet_from_input()
            shelter.add_pet(pet)
            print(colored("Pet added.", "green"))
        elif choice == '2':
            print("\nCurrent Inventory:")
            shelter.display_inventory()
        elif choice == '3':
            update_pet(shelter)
        elif choice == '4':
            delete_pet(shelter)
        elif choice == '5':
            save_to_file(shelter)
        elif choice == '6':
            load_from_file(shelter)
        elif choice == '7':
            print(colored("Exiting the program.","cyan"))
            break
        else:
            print(colored("Invalid choice, please try again.","red"))

