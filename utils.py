# utils.py
from termcolor import colored
import json
from pet_shelter import Pet

def add_pet_from_input():
    name = input("Enter pet's name: ")
    species = input("Enter pet's species (e.g., Dog, Cat): ")
    age = input("Enter pet's age: ")
    breed = input("Enter pet's breed (optional, press Enter to skip): ")

    pet = Pet(name=name, species=species, age=int(age), breed=breed if breed else None)
    return pet

def display_menu():
    print(colored("\n--- Pet Shelter Menu ---", attrs=["bold"]))
    print("1. Add Pet")
    print("2. View Pets")
    print("3. Update Pet")
    print("4. Delete Pet")
    print("5. Save to File")
    print("6. Load from File")
    print(colored("7. Exit","red"))

def update_pet(shelter):
    pet_name = input("Enter the name of the pet to update: ")
    pet = shelter.find_pet_by_name(pet_name)
    if pet:
        print(f"Current details: {pet}")
        new_name = input("Enter new name (or press Enter to keep current): ")
        new_species = input("Enter new species (or press Enter to keep current): ")
        new_age = input("Enter new age (or press Enter to keep current): ")
        new_breed = input("Enter new breed (or press Enter to keep current): ")

        if new_name:
            pet.name = new_name
        if new_species:
            pet.species = new_species
        if new_age:
            pet.age = int(new_age) if new_age else pet.age
        if new_breed:
            pet.breed = new_breed
        print(f"Updated pet details: {pet}")
    else:
        print("Pet not found.")

def delete_pet(shelter):
    pet_name = input("Enter the name of the pet to delete: ")
    pet = shelter.find_pet_by_name(pet_name)
    if pet:
        shelter.inventory.remove(pet)
        print(f"Pet {pet_name} has been deleted.")
    else:
        print("Pet not found.")

def save_to_file(shelter, filename='pets.json'):
    with open(filename, 'w') as f:
        json_data = [pet.__dict__ for pet in shelter.inventory]
        json.dump(json_data, f, indent=4)
    print(f"Data saved to {filename}.")

def load_from_file(shelter, filename='pets.json'):
    try:
        with open(filename, 'r') as f:
            json_data = json.load(f)
            shelter.inventory = [Pet(**data) for data in json_data]
        print(f"Data loaded from {filename}.")
    except FileNotFoundError:
        print(f"{filename} not found. Starting with an empty inventory.")
    except json.JSONDecodeError:
        print(f"Error reading {filename}. The file may be corrupted.")
