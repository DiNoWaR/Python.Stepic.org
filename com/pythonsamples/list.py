fruits = ["banana", "apple", "grape"]
vegetables = ["carrot", "cucumber", "tomato"]

# Adds an element at the end of the list
fruits.append("peach")
print(fruits)

# Adds an element at the specified position
fruits.insert(7, "orange")
print(fruits)

# Removes the first item with the specified value
fruits.remove("banana")
print(fruits)

# Removes the element at the specified position
fruits.pop()
print(fruits)

# Concatenates 2 lists
print(fruits + vegetables)

# Sorts list
fruits.sort()
print(fruits)

# Reverses the order of the list
fruits.reverse()
print(fruits)

# Returns a copy of the list
fruits_copy = fruits.copy()
print(fruits_copy)


for fruit in fruits:
   print(fruit)

