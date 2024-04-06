import json

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} кушает.")


class Bird(Animal):
    def make_sound(self):
        return f"{self.name} чирчикает."


class Mammal(Animal):
    def make_sound(self):
        return f"{self.name} рычит."


class Reptile(Animal):
    def make_sound(self):
        return f"{self.name} шипит."


def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append({'type': type(staff_member).__name__, 'name': staff_member.name})

    def save_to_file(self):
        with open('settings.txt', 'w') as file:
            # Convert objects to dictionaries before saving
            animals_data = [{'type': type(animal).__name__, 'name': animal.name, 'age': animal.age} for animal in self.animals]
            json.dump({'animals': animals_data, 'staff': self.staff}, file, indent=4)

    def load_from_file(self):
        with open('settings.txt', 'r') as file:
            data = json.load(file)
            self.animals = []
            for animal_data in data['animals']:
                # Reconstruct animals from dictionaries
                if animal_data['type'] == 'Bird':
                    self.animals.append(Bird(animal_data['name'], animal_data['age']))
                elif animal_data['type'] == 'Mammal':
                    self.animals.append(Mammal(animal_data['name'], animal_data['age']))
                elif animal_data['type'] == 'Reptile':
                    self.animals.append(Reptile(animal_data['name'], animal_data['age']))
            self.staff = data['staff']


class ZooKeeper:
    def feed_animal(self, animal):
        animal.eat()  # Corrected to call the eat method


class Veterinarian:
    def heal_animal(self, animal):
        print(f"Лечим животное {animal.name}.")



zoo = Zoo()
zoo.add_animal(Bird("Чижик-Пыжик", 2))
zoo.add_animal(Mammal("Тигра", 4))
zoo.add_animal(Reptile("Крокодил Гена", 33))

keeper = ZooKeeper()
vet = Veterinarian()

animal_sound(zoo.animals)

for animal in zoo.animals:
    keeper.feed_animal(animal)
    vet.heal_animal(animal)

zoo.save_to_file()
zoo.load_from_file()