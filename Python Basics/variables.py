# this is comment - will ignored by Python Interpreter
# A comment is a programmer-readable explanation or annotation in the Python source code
# you just need to add '#` before the line to make it 'comment'.

# First comment
print ("Hello, World!") # Second comment

'''
This is a multiline
comment.
'''


# Python code to print "Hello, World!"
print ("Hello, World!")



# Python Variables :

#   - Python variables are the reserved memory locations used to store values with in a Python Program. 
#   - This means that when you create a variable you reserve some space in the memory.


# How to declare variables ?
counter = 50          # Creates an integer variable
miles   = 500.0       # Creates a floating point variable
name    = "Gufran"   # Creates a string variable

print(counter)
print(miles)
print(name)

# deleting python variables
# counter = 100
# print(counter)

# del counter
# print(counter) # this will produce this error -> NameError: name 'counter' is not defined


# How to get type of a variable ?
x = "Gufran"
y = 10
z = 10.10

print(type(x)) # <class 'str'> -> means string type data
print(type(y)) # <class 'int'> -> means integer type data
print(type(z)) # <class 'float'> -> means float(decimal) type data



# Type Casting (or type conversion) in  Python variables :
#  
#   - Type casting is simply the process of converting a value from one data type to another.

x = str(10)    # x will be '10'
y = int(10)    # y will be 10 
z = float(10)  # z will be 10.0

print( "x =", x )
print( "y =", y )
print( "z =", z )



# Case Sensitivity of variables :

#    In python and many programming languages, variables are case sensitive

age = 20
Age = 30

print("age =", age) # 20
print("Age =", Age) # 30



# Multiple assignment  variables :

#   Python allows to initialize more than one variables in a single statement. 

a = b = c = 100

print (a)   # 100
print (b)   # 100
print (c)   # 100

# You can also assign multiple objects to multiple variables. For example −
a,b,c = 1,2,"Gufran"

print (a)   # 1
print (b)   # 2
print (c)   # Gufran


# Python variable naming convention (Rule to declare variables) :

#   - Every Python variable should have a unique name.
#   - A variable name can be meaningful like color, age, name etc.

#   - There are certain rules which should be taken care while naming a Python variable:
#       - A variable name must start with a letter or the underscore character
#       - A variable name cannot start with a number or any special character like $, (, * % etc.
#       - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#       - variable names are case-sensitive 
#           - which means Name and NAME are two different variables in Python.
#       - Python reserved keywords cannot be used naming the variable.

#   -  we should use these naming patterns −
#       - Camel case : For example: kmPerHour, pricePerLitre
#       - Pascal case : For example: KmPerHour, PricePerLitre
#       - Snake case : For example: km_per_hour, price_per_litre

counter = 100
_count  = 100
name1 = "Gufran"
name2 = "Alex"
Age  = 20
gufran_salary = 100000

print (counter)            # 100
print (_count)             # 100
print (name1)              # Gufran
print (name2)              # Alex
print (Age)                # 20
print (gufran_salary)      # 100000


# # Invalid python variables:

# 1counter = 100
# $_count  = 100
# zara-salary = 100000

# print (1counter)
# print ($count)
# print (zara-salary)

# # This will produce the following result:

# # File "main.py", line 3
# #     1counter = 100
# #            ^
# # SyntaxError: invalid syntax



# Benifits of variable :

#   - you declare once and can use repeatedly
# for example :
width = 10
height = 20
area = width*height
perimeter = 2*(width+height)
print ("Area = ", area)             # Area = 200 
print ("Perimeter = ", perimeter)   # Perimeter = 60



# Python Local Variables :

#   - Python Local Variables are defined inside a function. 
#   - We can not access variable outside the function.
#   - for example:
def sum(x,y):
   sum = x + y
   return sum

print(sum(5, 10))   # 15



# Python Global Variables :

#   - Any variable created outside a function can be accessed within any function,
#   - so they have global scope.
#   - for example:
x = 5
y = 10
def sum():
   sum = x + y
   return sum

print(sum())    # 15



# Constants in Python :
#   - Python doesn't have any formally defined constants, 
#   - However you can indicate a variable to be treated as a constant 
#       - by using all-caps names with underscores.
#   - For example, 
#       - the name PI_VALUE indicates that :
#           - you don't want the variable redefined or changed in any way.



# Python vs C/C++ Variables :
# 
#   - The concept of variable works differently in Python than in C/C++. In C/C++, 
#   - In C and C++, 
#     - a variable is like a box with a fixed label. 
#     - When you declare int x = 5;, 
#        - the computer carves out a specific spot in memory, labels it x, and puts the number 5 inside. 
#     - If you later change it to x = 10;, you are replacing the contents of that same box.


#   1. The "Box" vs "Tag" :
#       - C/C++ (Box): The variable is the memory location. It has a fixed type (like int) and can only hold that type of data.
#       - Python (Tag): The data itself (like the number 5) is an object that exists in memory. The variable name is just a label you "stick" onto that object.


#   2. Changing Values :
#       - C/C++: If you change a variable's value, the data at that specific memory address is overwritten.
#       - Python: If you say x = 5 and then x = 10, Python creates a new object (10) and moves the "x" tag from the 5 object to the 10 object. The original 5 stays in memory until Python's garbage collector cleans it up.

#   3. Static vs. Dynamic Typing :
#       - C/C++ (Static): You must tell the computer the type beforehand (int x). You cannot suddenly store a string in an integer "box."
#       - Python (Dynamic): Since the variable is just a tag, you can move it from an integer to a string whenever you want (x = 5 followed by x = "hello").


# The Python "Tagging" Process :
# Assign x = 5: Python creates an integer object 5 at a specific memory address and points the tag x to it.
# Reassign x = 10: Python doesn't change the 5. Instead, it creates a new integer object 10 and moves the tag x to this new address.
# for example:
x = 5
addr1 = id(x)
x = 10
addr2 = id(x)  # id() used to show memory address

print("Address of 5:", addr1)
print("Address of 10:", addr2)
print("Are they the same?", addr1 == addr2)
