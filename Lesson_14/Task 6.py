# Багатоуровневе наслідування

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def display_info(self):
        print(f'Animal: {self.name}\n'
              f'Species: {self.species}')


class Mammal(Animal):
    def __init__(self, name, species, nutrition):
        super().__init__(name, species)
        self.nutrition = nutrition

    def display_info(self):
        super().display_info()
        print(f'Diet Type: {self.nutrition}')


class Carnivore(Mammal):
    def __init__(self, name, species, nutrition, teeth):
        super().__init__(name, species, nutrition)
        self.teeth = teeth

    def display_info(self):
        super().display_info()
        print(f'Teeth Count: {self.teeth}')


class Lion(Carnivore):
    def __init__(self, name, species, nutrition, teeth, mane_size):
        super().__init__(name, species, nutrition, teeth)
        self.mane_size = mane_size

    def display_info(self):
        super().display_info()
        print(f'Mane Size: {self.mane_size}')


# Створюємо об'єкти різних класів
lion = Lion("Simba", "Lion", "Carnivore", 30, "Large")
carnivore = Carnivore("Tiger", "Carnivore", "Carnivore", 40)
mammal = Mammal("Elephant", "Mammal", "Herbivore")

# Виводимо інформацію про кожну тварину
lion.display_info()
print("-------------------------")
carnivore.display_info()
print("-------------------------")
mammal.display_info()