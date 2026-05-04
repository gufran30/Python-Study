# Tuples :

# Tuple is one of the built-in data types in Python. 
# A Python tuple is a sequence of comma separated items, enclosed in parentheses (). 
# The items in a Python tuple need not be of same data type.
tup1 = ("Alex", "Physics", 21, 69.75)
tup2 = (1, 2, 3, 4, 5)
tup3 = ("a", "b", "c", "d")
tup4 = (25.50, True, -55, 1+2j)


# note : Even if there is only one object in a tuple, you must give a comma after it. Otherwise, it is treated as a string.

# ======================================================================

# Accessing Values in Tuples
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print ("tup1[0]: ", tup1[0]);   # tup1[0]:  physics
print ("tup2[1:5]: ", tup2[1:5]);   # tup2[1:5]:  [2, 3, 4, 5]

# ======================================================================

# Updating Tuples :

# Tuples are immutable which means you cannot update or change the values of tuple elements. 
# You are able to take portions of existing tuples to create new tuples as the following example demonstrates −

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print (tup3);   # (12, 34.56, 'abc', 'xyz')


# ======================================================================

# Delete Tuple Elements :

# Removing individual tuple elements is not possible.

# To explicitly remove an entire tuple, just use the del statement. For example −
tup = ('physics', 'chemistry', 1997, 2000);
print (tup);    # ('physics', 'chemistry', 1997, 2000)
del tup;
# print ("After deleting tup : ");
# print (tup);    # NameError: name 'tup' is not defined


# ======================================================================

# Python Tuple Operations :

# In Python, Tuple is a sequence. 
# Hence, we can concatenate two tuples with + operator and concatenate multiple copies of a tuple with "*" operator. 
# The membership operators "in" and "not in" work with tuple object.

# Concatenation
print((1, 2, 3) + (4, 5, 6))    # (1, 2, 3, 4, 5, 6)

# Repetition
print(('Hi!',) * 4) # ('Hi!', 'Hi!', 'Hi!', 'Hi!')

# Membership
print(3 in (1, 2, 3))   # 


# ======================================================================

# Indexing, Slicing, and Matrixes :

# Because tuples are sequences, indexing and slicing work the same way for tuples as they do for strings. Assuming following input −

L = ('spam', 'Spam', 'SPAM!')

print(L[2]) # SPAM!
print(L[-2])    # Spam
print(L[1:])    # ('Spam', 'SPAM!')


# ======================================================================

# No Enclosing Delimiters :

# Any set of multiple objects, comma-separated, written without identifying symbols, i.e., brackets for lists, parentheses for tuples, etc., default to tuples, as indicated in these short examples −

print ('abc', -4.24e93, 18+6.6j, 'xyz');    # abc -4.24e+93 (18+6.6j) xyz
x, y = 1, 2;
print ("Value of x , y : ", x,y);   # Value of x , y : 1 2


# ======================================================================

# Tuple Methods :

# 1. count()
#   - This method returns the number of times a specific value appears in the tuple.
#   - Syntax: tuple.count(value)

my_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# Count how many times the number 7 appears
result = my_tuple.count(7)
print(result)  # Output: 2


# 2. index()
#   - This method finds the first occurrence of a specific value and returns its position (index). If the value is not found, it raises a ValueError.
#   - Syntax: tuple.index(value)

fruits = ('apple', 'banana', 'cherry', 'banana')

# Find the index of the first 'banana'
pos = fruits.index('banana')
print(pos)  # Output: 1

# ======================================================================

# Built-in Functions Used with Tuples

# len()     Returns the number of items.                        len((1, 2, 3)) → 3
# max()     Returns the largest element.                        max((10, 20, 5)) → 20
# min()     Returns the smallest element.                       min((10, 20, 5)) → 5
# sum()     Adds all numeric elements.                          sum((1, 2, 3)) → 6
# sorted()   Returns a new list with items in order.             sorted((3, 1, 2)) → [1, 2, 3]
# tuple()   Converts an iterable (like a list) into a tuple.    tuple([1, 2]) → (1, 2)
