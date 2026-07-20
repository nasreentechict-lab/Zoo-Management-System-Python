# List to store animal names
animals = ["Lion", "Elephant", "Bird"]

# Function to display all animals in the list
def display_animals():
    # Counter for numbering the animals
    i = 1

    # Loop through each animal in the list
    for animal in animals:
        print(i, animal)
        i += 1

# Call the function to display the initial list
display_animals()

# Print a separator line
print('-------------------')


# Function to add a new animal
def add_animal(animal):

    # Check if the animal is not already in the list
    if animal not in animals:
        animals.append(animal)
        print("Animal Added Successfully")
    else:
        # Display a message if the animal already exists
        print("Animal already exists")


# Add a new animal
add_animal('Zebra')

# Display the updated list
display_animals()

# Print a separator line
print('-------------------')

# Try adding an existing animal
add_animal('Lion')
