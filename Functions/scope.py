# scope

# A variable is only available from inside the region it is created. This is called scope.


# ===========================================================================================

# Local Scope :

#   - A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

# example : A variable created inside a function is available inside that function:

def my_func():
    x = 300
    print(x)

my_func()   # 300


# ----------------------------------------------------------------------------------------

# Function Inside Function  :

#   - As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:

def my_func():
    x = 300
    def my_inner_func():
        print(x)
    my_inner_func()

my_func()   # 300


# ===========================================================================================

# Global Scope :

#   - A variable created in the main body of the Python code is a global variable and belongs to the global scope.
#   - Global variables are available from within any scope, global and local.


# example : A variable created outside of a function is global and can be used by anyone:

x = 300

def myfunc():
  print(x)

myfunc()    # 300
print(x)    # 300


# ===========================================================================================

# Naming Variables  :

# If you operate with the same variable name inside and outside of a function, 
#   - Python will treat them as two separate variables, 
#   - one available in the global scope (outside the function) 
#   - and one available in the local scope (inside the function):

# example : The function will print the local x, and then the code will print the global x:

x = 300

def my_func():
    x = 200
    print(x)    # 200

my_func()
print(x)    # 300


# ===========================================================================================

# Global Keyword
#   - If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
#   - The global keyword makes the variable global.

# example : If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = 300

myfunc()
print(x)    # this will not throw error because x become global so you can access it from anywhere


# --------------------------------------------------------

# Also, use the global keyword if you want to make a change to a global variable inside a function.

# example : To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = 300

def myfunc():
  global x
  x = 200

myfunc()
print(x)    # 200


# ===========================================================================================


# Nonlocal Keyword :

#   - The nonlocal keyword is used to work with variables inside nested functions.
#   - The nonlocal keyword makes the variable belong to the outer function.


# example : If you use the nonlocal keyword, the variable will belong to the outer function:

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())    # hello


# ===========================================================================================

# The LEGB Rule
#   - Python follows the LEGB rule when looking up variable names, and searches for them in this order:

#       1. Local - Inside the current function
#       2. Enclosing - Inside enclosing functions (from inner to outer)
#       3. Global - At the top level of the module
#       4. Built-in - In Python's built-in namespace


# understanding the LEGB rule :

x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)  # Inner: local
  inner()
  print("Outer:", x)    # Outer: enclosing

outer()
print("Global:", x) # Global: global