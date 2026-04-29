# Python Data Types :

#   - In general, the data types are used to define the type of a variable. 
#   - It represents the type of data we are going to store in a variable and determines what operations can be done on it.
#   - Because everything in Python is an object, 
#       - these data types are technically classes, and variables are instances (object) of those classes
#   - Since Python is dynamically typed, 
#       - the data type of a variable is determined at runtime based on the assigned value.


# ============================================================================================


# Types of Data Types in Python :

# Python supports the following built-in data types −

# Numeric Data Types
#   - int
#   - flot
#   - complex

# String Data Types

# Sequence Data Types
#   - list
#   - tuple
#   - range

# Binary Data Types
#   - bytes
#   - bytearray
#   - memoryview

# Dictionary Data Type

# Set Data Type
#   - set
#   - frozenset

# Boolean Data Type
# None Type


# ============================================================================================


# 1. Python Numeric Data Types

# Python numeric data types store numeric values. Number objects are created when you assign a value to them
# For example −
var1 = 1       # int data type
var2 = True    # bool data type
var3 = 10.023  # float data type
var4 = 10+3j   # complex data type

# Example of Numeric Data Types :

# integer variable.
a = 100
print("The type of variable having value", a, " is ", type(a))  # <class 'int'> means int type

# float variable.
c = 20.345
print("The type of variable having value", c, " is ", type(c))  # <class 'float'> means float(decimal) type

# complex variable.
d = 10+3j
print("The type of variable having value", d, " is ", type(d))  # <class 'complex'> means complex type


# ============================================================================================



# 2. Python String Data Type :

#   - Python string is a sequence of one or more Unicode characters, enclosed in single, double or triple quotation marks (also called inverted commas). 
#   - Python strings are immutable which means when you perform an operation on strings, you always produce a new string object of the same type, rather than mutating an existing string.

str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string


# ============================================================================================



# 3. Python Sequence Data Types :
#   - Sequence is a collection data type. It is an ordered collection of items.
#   - Items in the sequence have a positional index starting with 0.
#   - It is conceptually similar to an array in C or C++. 
#   - There are following three sequence data types defined in Python.
#       - List Data Type
#       - Tuple Data Type
#       - Range Data Type

# note : Python sequences are bounded and iterable - 
#           - Whenever we say an iterable in Python, 
#                   - it means a sequence data type (for example, a list).



# a) Example of List Data Type :
#       - A Python list contains items separated by commas and enclosed within square brackets ([])
#       - 

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists

# b) Example of Python Tuple Data Type :
#       - A Python tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses (...)

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples

# NOTE - the main difference in tuple & list are :    
#       - Lists are mutable: 
#               - Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed
#       - Tuple are immutable 
#               - tuples are enclosed in parentheses ( ( ) ) and cannot be updated (immutable). 
#               - Tuples can be thought of as read-only lists.

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list



# c) Python Range Data Type :
#       - range is an immutable sequence of numbers 
#       - which is typically used to iterate through a specific number of items.
#       - It is represented by the Range class. 
#       - syntax:  range(start, stop, step)
#           - start : Integer number to specify starting position, (Its optional, Default: 0)
#           - stop  : Integer number to specify ending position (It's mandatory)
#           - step  : Integer number to specify increment, (Its optional, Default: 1)

for i in range(5):
  print(i) 

# above code produce the following result :
# 0
# 1
# 2
# 3
# 4

for i in range(2, 5):
  print(i)

# above code produce the following result :
# 2
# 3
# 4

for i in range(1, 5, 2):
  print(i)

# above code produce the following result :
# 1
# 3



# ============================================================================================



# 4. Python Binary Data Types :
#   - A binary data type in Python is a way to represent data as a series of binary digits, which are 0's and 1's. 
#   - It is like a special language computers understand to store and process information efficiently.
#   - This type of data is commonly used when dealing with things like files, images, or anything that can be represented using just two possible values. 
#   - So, instead of using regular numbers or letters, binary sequence data types use a combination of 0s and 1s to represent information.

# Python provides three different ways to represent binary data. They are as follows −
#   - bytes
#   - bytearray
#   - memoryview


# ============================================================================================



# 5. Python Dictionary Data Type
#   - Python dictionaries are kind of hash table type.
#   - data stored in key-value pairs2 +
#   - A dictionary key can be almost any Python type, but are usually numbers or strings. 
#   - Values, on the other hand, can be any arbitrary Python object.

# Example of Dictionary Data Type

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values


# ============================================================================================



# 6. Python Set Data Type
#   - Set is a Python implementation of set as defined in Mathematics.
#   - A set in Python is a collection, but is not an indexed or ordered collection as string, list or tuple.
#   - An object cannot appear more than once in a set, whereas in List and Tuple, same object can appear more than once.
set1 = {123, 452, 5, 6}
set2 = {'Java', 'Python', 'JavaScript'}

print(set1) # {123, 452, 5, 6}
print(set2) # {'Python', 'JavaScript', 'Java'}


# ============================================================================================



# 7. Python Boolean Data Type
#   - Python boolean type is one of built-in data types which represents one of the two values either True or False. 
#   - Python bool() function allows you to evaluate the value of any expression and returns either True or False based on the expression.
#   - for example :
a = True
# display the value of a
print(a)

# display the data type of a
print(type(a))

# Returns false as a is not equal to b
a = 2
b = 4
print(bool(a==b))

# Following also prints the same
print(a==b)


# ============================================================================================



# 8. Python None Type
#   - Python's none type is represented by the "nonetype." 
#   - It is an object of its own data type. 
#   - The nonetype represents the null type of values or absence of a value.

# Declaring a variable
# And, assigning a Null value (None)

x = None

# Printing its value and type
print("x = ", x)    # x =  None
print("type of x = ", type(x))  # type of x =  <class 'NoneType'>