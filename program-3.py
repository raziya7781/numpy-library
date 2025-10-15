# Base class
class Animal:
    def make_sound(self):
        print("Animal makes a sound")

# Derived class: Dog
class Dog(Animal):
    def make_sound(self):
        print("Dog says: Woof!")

# Derived class: Cat
class Cat(Animal):
    def make_sound(self):
        print("Cat says: Meow!")

# Derived class: Bird
class Bird(Animal):
    def make_sound(self):
        print("Bird says: Tweet!")


# List of different animal objects
animals = [Dog(), Cat(), Bird()]

# Polymorphism: same method behaves differently for each object
for animal in animals:
    animal.make_sound()
