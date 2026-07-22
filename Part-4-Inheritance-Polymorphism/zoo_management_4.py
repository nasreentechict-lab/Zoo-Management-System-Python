# ============================
# Base Class
# ============================

# Define the Animal class
class Animal:

    # Constructor to initialize the object's attributes
    def __init__(self, name, age, weight):

        # Public attributes
        self.name = name
        self.age = age

        # Private attribute (Encapsulation)
        self.__weight = weight

    # Method that can be overridden by child classes
    def make_sound(self):
        print("Some animal sound")


# ============================
# Child Class: Lion
# ============================

# Lion inherits from Animal
class Lion(Animal):

    # Override the make_sound() method
    def make_sound(self):
        print("Roar")


# Create a Lion object
lion = Lion("Simba", 5, 120.5)

# Access inherited public attribute
print(lion.name)


# ============================
# Child Class: Bird
# ============================

# Bird inherits from Animal
class Bird(Animal):

    # Bird-specific method
    def fly(self):
        print("Flying...")

    # Override the make_sound() method
    def make_sound(self):
        print("Tweet")


# Create a Bird object
bird = Bird("Eagle", 3, 3)

# Call Bird-specific method
bird.fly()

print("------ Polymorphism ------")

# Store different objects in the same list
animals = [
    Lion("Simba", 5, 120.5),
    Bird("Eagle", 3, 2)
]

# Polymorphism:
# The same method call behaves differently
# depending on the object's actual type.
for animal in animals:
    animal.make_sound()
