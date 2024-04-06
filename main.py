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
        self.staff.append(staff_member)


class ZooKeeper:
    def feed_animal(self, animal):
        print(f"Кормим животное {animal.name}.")


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