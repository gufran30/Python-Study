# Function 

# - Function is a reusable block of code designed to perform a specific task.
# - Functions help you organize code, avoid repetition (following the "Don't Repeat Yourself" or DRY principle), and make programs more modular.

# - A Python function may be invoked from any other function by passing required data (called parameters or arguments)

# - A function is a block of code which only runs when it is called.
# - A function can return data as a result.
# - A function helps avoiding code repetition.

# ============================================================================================

# Creating a functon :

# In Python, a function is defined using the def keyword, followed by a function name and parentheses:

# example :
def my_function():
    print("Hello from a function")

# This creates a function named my_function that prints "Hello from a function" when called.
# The code inside the function must be indented. Python uses indentation to define code blocks.

# ============================================================================================

# Calling a Function :

def my_function():
  print("Hello from a function")

my_function()

# You can call the same function multiple times:

def my_function():
  print("Hello from a function")

my_function()
my_function()
my_function()

# ============================================================================================

# Function Names :

# Function names follow the same rules as variable names in Python:

#   - A function name must start with a letter or underscore
#   - A function name can only contain letters, numbers, and underscores
#   - Function names are case-sensitive (myFunction and myfunction are different)

# Example
# Valid function names:

# calculate_sum()
# _private_function()
# myFunction2()

# It's good practice to use descriptive names that explain what the function does.


# ============================================================================================

# Why Use Functions?

# Imagine you need to convert temperatures from Fahrenheit to Celsius several times in your program. Without functions, you would have to write the same calculation code repeatedly:

# Example :
# Without functions - repetitive code:
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

# With functions, you write the code once and reuse it:

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))


# Return Values

# Functions can send data back to the code that called them using the return statement.
# When a function reaches a return statement, it stops executing and sends the result back:

# for example :
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

# If a function doesn't have a return statement, it returns None by default.