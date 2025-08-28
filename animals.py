# Base class
class Animal:
    def move(self):
        print("This animal moves in some way.")

# Derived classes
class Dog(Animal):
    def move(self):
        print("Dog runs on four legs 🐕")

class Bird(Animal):
    def move(self):
        print("Bird flies in the sky 🕊️")

class Fish(Animal):
    def move(self):
        print("Fish swims in water 🐟")

# Polymorphism in action
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()
