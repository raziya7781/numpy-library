# Base class
class Animal:
    def speak(self):
        print("Animal speaks")

# Derived class: Dog
class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")

# Derived class: Cat
class Cat(Animal):
    def speak(self):
        print("Cat says: Meow!")

# Create objects
d = Dog()
c = Cat()

# Call methods
d.speak()   # Output: Dog says: Woof!
c.speak()   # Output: Cat says: Meow!
