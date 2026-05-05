# Types of Python Functions

#   1. Built-in functions :
#       - Python's standard library includes number of built-in functions. 
#       - Some of Python's built-in functions are :
#            print(), int(), len(), sum(), etc.

#   2. Functions defined in built-in modules :
#       - The standard library also bundles a number of modules. 
#       - Each module defines a group of functions. 
#       - These functions are not readily available. 
#       - You need to import them into the memory from their respective modules.

#   3. User-defined functions :
#       - In addition to the built-in functions and functions in the built-in modules, you can also create your own functions. 
#       - These functions are called user-defined functions. 

# ======================================================================

# Syntax to Define a Python Function

# def function_name( parameters ):
#    "function_docstring"
#    function_suite
#    return [expression]

# Example to Define a Python Function
def greetings():
   "This is docstring of greetings function"
   print ("Hello World")
   return

# When this function is called, Hello world message will be printed.
greetings()     # Hello World


# ======================================================================

# Example to Call a Python Function

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

# Now you can call the function
printme("I'm first call to user defined function!") # I'm first call to user defined function!
printme("Again second call to the same function")   # Again second call to the same function


# ======================================================================

# Pass by Reference vs Value

# In programming languages like C and C++, 
# there are two main ways to pass variables to a function, 
# which are Call by Value and Call by Reference (also known as pass by reference and pass by value). 
# However, the way we pass variables to functions in Python differs from others.


# call by value  :
#   − When a variable is passed to a function while calling, the value of actual arguments is copied to the variables representing the formal arguments. Thus, any changes in formal arguments does not get reflected in the actual argument. This way of passing variable is known as call by value.

# call by reference :
#   − In this way of passing variable, a reference to the object in memory is passed. Both the formal arguments and the actual arguments (variables in the calling code) refer to the same object. Hence, any changes in formal arguments does get reflected in the actual argument.


# IN PYTHON :
# Python uses pass by reference mechanism. 
#   - As variable in Python is a label or reference to the object in the memory, both the variables used as actual argument as well as formal arguments really refer to the same object in the memory. 
#   - We can verify this fact by checking the id() of the passed variable before and after passing.


# Example
# In the following example, we are checking the id() of a variable.

def test_function(arg):
   print("ID inside the function:", id(arg))

greet = "hello"
print("ID before passing:", id(greet))  # ID before passing: 2601648611392
test_function(greet)    # ID inside the function: 2601648611392    



# Note :
# The behavior also depends on whether the passed object is mutable or immutable. 
#   - Python numeric object is immutable. 
#   - When a numeric object is passed, and then the function changes the value of the formal argument, it actually creates a new object in the memory, leaving the original variable unchanged.

# Example
# The following example shows how an immutable object behaves when it is passed to a function.

def test_function2(arg):
   print ("ID inside the function:", id(arg))   # ID before passing: 140706606893784
   arg = arg + 1
   print ("ID of new object after increment", arg, id(arg)) # ID inside the function: 140706606893784

var = 10
print ("ID before passing:", id(var))   # ID of new object after increment 11 140706606893816
test_function2(var)
print ("value after function call", var)    # value after function call 10