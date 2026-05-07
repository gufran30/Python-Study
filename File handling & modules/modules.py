# Modules in Python 
# ---------------------

# - In Python, a module is simply a file containing Python code—like functions, classes, and variables—that you can reuse in other programs. 
# - They help you organize large projects into smaller, manageable parts.

# ======================================================================================

# Types of Modules 
# -----------------------------------

# Built-in Modules: 
#   - These come pre-installed with Python, such as math, os, sys, and random.
# 
# User-Defined Modules: 
#   - Files you create yourself (e.g., mymodule.py) to store your own logic.

# External Modules: 
#   - Third-party libraries like NumPy, Pandas, or Requests that you install using pip.


# ======================================================================================

# Example of Python Module
import math
print("Square root of 100:", math.sqrt(100))    # Square root of 100: 10.0

# ======================================================================================

# Python Built-in Modules

# os :
#   - This module provides a unified interface to a number of operating system functions.

# random :
#   - Generate pseudo-random numbers

# sys :
#   - Provides functions that acts strongly with the interpreter.

# math :
#   - This module implements a number of mathematical operations for floating point numbers. These functions are generally thin wrappers around the platform C library functions.

# cmath :
#   - This module contains a number of mathematical operations for complex numbers.

# statistics :
#   - Mathematical statistics functions

# json 
#   - Encode and decode the JSON format.


# ======================================================================================

# Python User-defined Modules

#   - Any text file with .py extension and containing Python code is basically a module. 
#   - It can contain definitions of one or more functions, variables, constants as well as classes.
#   - It can contain definitions of one or more functions, variables, constants as well as classes

# ---------------------------------------------------------------------------------------

# Creating a Python Module

# - Creating a module is nothing but saving a Python code with the help of any editor. Let us save the following code as mymodule.py

def SayHello(name):
    print("Hi {}! How are you ?".format(name))
    return

# now you can import this above code as module in another python script

import mymodule
mymodule.SayHello("Alex")   # Hi Harish! How are you?

# ---------------------------------------------------------------------------------------

# The import Statement
#   - In Python, the import keyword has been provided to load a Python object from one module.
#   - The object may be a function, class, a variable etc. 
#   - If a module contains multiple definitions, all of them will be loaded in the namespace.

#   - Let us save the following code having three functions as mymodule.py.
def sum(x,y):
   return x+y

def average(x,y):
   return (x+y)/2

def power(x,y):
   return x**y

# To call any function, use the module object's reference. For example, mymodule.sum().
import mymodule
print ("sum:",mymodule.sum(10,20))
print ("average:",mymodule.average(10,20))
print ("power:",mymodule.power(10, 2))

# It will produce the following output −

# sum:30
# average:15.0
# power:100


# ---------------------------------------------------------------------------------------

# The from ... import Statement

# - The import statement will load all the resources of the module in the current namespace. 
# - It is possible to import specific objects from a module by using this syntax. 

# For example −
#   - Out of three functions in mymodule, only two are imported in following executable script example.py

from mymodule import sum, average
print ("sum:",sum(10,20))
print ("average:",average(10,20))

# It will produce the following output −
# sum: 30
# average: 15.0

# ---------------------------------------------------------------------------------------

# The from...import * Statement
#   - It is also possible to import all the names from a module into the current namespace by using the following import statement −

from modname import *
