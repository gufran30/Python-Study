# Dictionaries in Python

# In Python, a dictionary is a built-in data type that stores data in key-value pairs. 
# It is an unordered, mutable, and indexed collection. 
# Each key in a dictionary is unique and maps to a value.

#  Dictionaries are often used to store data that is related, 
#   - such as information associated with a specific entity or object, 
#   - where you can quickly retrieve a value based on its key.


# Python's dictionary is an example of a mapping type

# Each key-value pair is separated by a comma and enclosed within curly braces {}.
# The key and value within each pair are separated by a colon (:), forming the structure key:value.

# =======================================================================

# 1. Create a dictionary
#   - You define a dictionary using curly braces {} with keys and values separated by a colon :

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Access a value using its key
print(car["model"])  # Output: Mustang

# =======================================================================

# 2. Modifying and Adding Items
#   - You can update an existing value or add a new pair simply by assigning a value to a key

#  Update an existing key
car["year"] = 2024

# Add a new key-value pair
car["color"] = "Red"

print(car) 
# Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2024, 'color': 'Red'}

# =======================================================================

# 3. Removing Items
#   - You can use del to delete a specific item or .pop() to remove an item and return its value

# =======================================================================

# Key Features of Dictionaries
#   - Unordered 
#   - Mutable : You can change, add, or remove items after the dictionary has been created.
#   - Indexed : Although dictionaries do not have numeric indexes, they use keys as indexes to access the associated values.

#   - Unique keys :  Each key in a dictionary must be unique. If you try to assign a value to an existing key, the old value will be replaced by the new value.

#   - Heterogenous : Keys and values in a dictionary can be of any data type.


# =======================================================================

# 4. Iterating Through a Dictionary
#   - You can loop through keys, values, or both simultaneously using methods like .keys(), .values(), or .items().

user = {"name": "Alice", "age": 25, "city": "NYC"}

# Loop through keys and values together
for key, value in user.items():
    print(f"{key}: {value}")

# output :
# name: Alice
# age: 25
# city: NYC


# Essential Dictionary Methods
# 
# Method         Description
# .get(key)      Returns the value for a key; returns None if the key is missing.
# .keys()        Returns a list-like view of all keys in the dictionary.
# .values()      Returns a list-like view of all values.
# .items()       Returns a list of tuples for each key-value pair.
# .update()      Merges another dictionary or iterable into the current one.
