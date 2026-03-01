''' Demonstrating how lists work '''

# Lists are used to store multiple pieces of information
# We use square brackets to show it is a list
# Items are separated by commas
names = ["Ace", "Chopper", "Luffy", "Nami", "Sanji", "Usopp", "Zoro"]

# Print the entire list
# This is useful for debugging
print(names)

# Each item has an index, its location in the list.
# The first item has an index of zero
# We can print individual items from a list by using their index
print(names[6])
# Using a negative index counts backwards from the end
# -1 prints the last item, -2 the second last, etc
print(names[-1])

# We can use len() to get the number of items in a list
length = len(names)
# Here we print out the length of an item in the list
print(len(names[0]))

# To change an item, just overwrite it by setting a new value for that position in the list
names[4] = "White Beard"
print(names)

# You can insert items into a particular position in a list
names.insert(1, "Sanji")
print(names)

# The most common method of adding items is to add them at the end using append()
names.append("Robin")
print(names)

# When displaying all items from a list it is best to use a loop rather than printing the whole list with brackets and commas
# Method 1: displaying each item
for name in names:
    print(name)

# Method 2: displaying items in a numbered list

for i in range(len(names)):
    print(f"{i+1} {names[i]}")
