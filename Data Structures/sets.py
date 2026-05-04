# Sets 

# In Python, a set is an unordered collection of unique elements. 
# Unlike lists or tuples, sets do not allow duplicate values 
#   - i.e. each element in a set must be unique. 
# Sets are mutable, meaning you can add or remove items after a set has been created.

# Sets are defined using curly braces {} or the built-in set() function. 
# They are particularly useful for membership testing, removing duplicates from a sequence, and performing common mathematical set operations like union, intersection, and difference.

# note : A set refers to a collection of distinct objects. It is used to group objects together and to study their properties and relationships. The objects in a set are called elements or members of the set.

# =================================================================

# Creating a Set in Python :

my_set = {1, 2, 3, 4, 5}
print (my_set)  # {1, 2, 3, 4, 5}

# using set() function
my_set = set([1, 2, 3, 4, 5])
print (my_set)


# =================================================================

# Duplicate Elements in Set

# Sets in Python are unordered collections of unique elements. 
# If you try to create a set with duplicate elements, duplicates will be automatically removed −

my_set = {1, 2, 2, 3, 3, 4, 5, 5} 
print (my_set)  # {1, 2, 3, 4, 5}


# Sets can contain elements of different data types, including numbers, strings, and even other sets (as long as they are immutable) −

mixed_set = {1, 'hello', (1, 2, 3)}
print (mixed_set)   # {1, 'hello', (1, 2, 3)}


# =================================================================

# Adding Elements in a Set ;

my_set = {1, 2, 3, 3}
# Adding an element 4 to the set
my_set.add(4)  
print (my_set)  # {1, 2, 3, 4}


# Removing Elements from a Set :

my_set = {1, 2, 3, 4}
# Removes the element 3 from the set
my_set.remove(3)  
print (my_set)  # {1, 2, 4}

# Alternatively, you can use the discard() function to remove an element from the set if it is present. 
# Unlike remove(), discard() does not raise an error if the element is not found in the set −

my_set = {1, 2, 3, 4}
# No error even if 5 is not in the set
my_set.discard(5)  
print (my_set)  # {1, 2, 3, 4}


# =================================================================

# Membership Testing in a Set :

my_set = {1, 2, 3, 4}
if 2 in my_set:
   print("2 is present in the set")
else:
   print("2 is not present in the set")

# output -  2 is present in the set


# =================================================================

# Set Operations

#  - In Python, sets support various set operations, which is used to manipulate and compare sets.

# - These operations include union, intersection, difference, symmetric difference, and subset testing. 

# - Sets are particularly useful when dealing with collections of unique elements and performing operations based on set theory.

# Union :
#   - It combine elements from both sets using the union() function or the | operator.

# Intersection :
#   − It is used to get common elements using the intersection() function or the & operator.

# Difference : 
#   − It is used to get elements that are in one set but not the other using the difference() function or the - operator.

# Symmetric Difference :
#   − It is used to get elements that are in either of the sets but not in both using the symmetric_difference() method or the ^ operator.


# =================================================================

# Python Set Comprehensions

# Set comprehensions in Python is a concise way to create sets based on iterable objects, similar to list comprehensions. 
# It is used to generate sets by applying an expression to each item in an iterable.

# Set comprehensions are useful when you need to create a set from the result of applying some operation or filtering elements from another iterable.


# Syntax :
# set_variable = {expression for item in iterable if condition}

# example
squared_set = { x**2 for x in range(1, 6)}
print(squared_set)  # {1, 4, 9, 16, 25}



# Filtering Elements Using Set Comprehensions

even_set = { x for x in range(1, 11) if x % 2 == 0}
print(even_set) # {2, 4, 6, 8, 10}



# Nested Set Comprehensions

# - Set comprehensions also support nested loops, allowing you to create sets from nested iterables. This can be useful for generating combinations or permutations of elements.

nested_set = { (x, y) for x in range(1, 3) for y in range(1, 3)}
print(nested_set)   # {(1, 1), (1, 2), (2, 1), (2, 2)}


# =================================================================

# Frozen Sets :

#   - In Python, a frozen set is an immutable collection of unique elements, 
#   - similar to a regular set but with the distinction that it cannot be modified after creation. 
#   - Once created, the elements within a frozen set cannot be added, removed, or modified, making it a suitable choice when you need an immutable set.


# You can create a frozen set in Python using the frozenset() function by passing an iterable (such as a list, tuple, or another set) containing the elements you want to include in the frozen set.

my_frozen_set = frozenset([1, 2, 3])
print(my_frozen_set)    # frozenset({1, 2, 3})

# my_frozen_set.add(4) - Error - AttributeError: 'frozenset' object has no attribute 'add'


