# *args and **kwargs


# If you do not know how many arguments will be passed into your function, add a * before the parameter name.
# This way, the function will receive a tuple of arguments and can access the items accordingly:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


# *args
#   - The *args parameter allows a function to accept any number of positional arguments.
#   - Inside the function, args becomes a tuple containing all the passed arguments:

# example
def my_function(*args):
  print("Type:", type(args))    # Type: <class 'tuple'>
  print("First argument:", args[0]) # First argument: Emil
  print("Second argument:", args[1])    # Second argument: Tobias
  print("All arguments:", args) # All arguments: ('Emil', 'Tobias', 'Linus')

my_function("Emil", "Tobias", "Linus")


# Using *args with Regular Arguments :

#   - You can combine regular parameters with *args.
#   - Regular parameters must come before *args:


# Example
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

# output:
# Hello Emil
# Hello Tobias
# Hello Linus

# In this example, "Hello" is assigned to greeting, and the rest are collected in names.



# Practical Example with *args
#   - *args is useful when you want to create flexible functions:


# Example
# A function that calculates the sum of any number of values:

def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3)) # 6
print(my_function(10, 20, 30, 40))  # 100
print(my_function(5))   # 5





# =======================================================================================

# kwargs :

# In Python, **kwargs (short for "keyword arguments") is a special syntax used in function definitions to accept an arbitrary number of keyworded arguments

# When you use **keyargs in a function signature, Python collects all extra named arguments passed into that function into a dictonary



# example :
def greet_users(**kwargs):
    # kwargs is a dictionary: {'Alice': 'Manager', 'Bob': 'Developer'}
    for name, role in kwargs.items():
        print(f"{name} is a {role}")

greet_users(Alice="Manager", Bob="Developer")


# Key Characteristics
#
# Dictionary Format: 
#   - Inside the function, kwargs is a standard Python dictionary where keys are the argument names and values are the passed values.

# Variable Length: 
#   - It allows you to pass any number of named arguments (e.g., name="Alice", age=30) without predefined parameters.

# Convention over Rule: 
#   - The name kwargs is just a convention; the double asterisks (**) are what actually enable this behavior. You could technically use **details or **options.

# Ordering: 
#   - In a function definition, **kwargs must always come last, after standard arguments and *args.


# Difference from *args :


# While **kwargs handles named (keyword) arguments as a dictionary, *args handles positional (unnamed) arguments as a 

# Argument Type         Positional (e.g., 1, 2, 3)          Keyword (e.g., a=1, b=2)
# Data Structure        Tuple                               Dictionary
# Syntax                Single asterisk *                   Double asterisk **