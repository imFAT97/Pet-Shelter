class Pet:
    def __init__(self, name, species, age, breed=None):
        self.name = name
        self.species = species
        self.age = age
        self.breed = breed

    def __str__(self):
        breed_info = f", Breed: {self.breed}" if self.breed else ""
        return f"Name: {self.name}, Species: {self.species}, Age: {self.age}{breed_info}"


class PetShelter:
    def __init__(self):
        self.inventory = []

    def add_pet(self, pet):
        self.inventory.append(pet)

    def display_inventory(self):
        if not self.inventory:
            print("No pets available.")
        else:
            for pet in self.inventory:
                print(pet)

    def find_pet_by_name(self, name):
        for pet in self.inventory:
            if pet.name.lower() == name.lower():
                return pet
        return None
