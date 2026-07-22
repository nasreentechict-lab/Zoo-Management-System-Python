
# Define the Animal class
class Animal:

    # Constructor to initialize the object's attributes
    def __init__(self, name, age, weight):

        # Public attributes
        self.name = name
        self.age = age

        # Private attribute (Encapsulation)
        self.__weight = weight

    # Method to display the animal's information
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Weight:", self.__weight)

    # Getter method to access the private weight
    def get_weight(self):
        return self.__weight

    # Setter method to update the private weight
    def update_weight(self, weight):

        # Validate the new weight before updating
        if weight > 0:
            self.__weight = weight
        else:
            print("Invalid weight")


# Create an Animal object
lion = Animal(
    "Simba",
    5,
    190.5
)

# Display the original information
lion.display_info()

print('---------------------')

# Try to update with an invalid weight
lion.update_weight(-120.4)

print('---------------------')

# Update with a valid weight
lion.update_weight(140)

# Display the updated information
lion.display_info()
