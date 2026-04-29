# Python String Methods

# Python string methods is a collection of in-built Python functions that operates on strings.

# Note: Every string method in Python does not change the original string instead returns a new string with the changed attributes. 

# ============================================================================================

# .split() : 

#   - Split a string into a list where each word is a list item.
txt = "welcome to the jungle"
x = txt.split()
print(x)    # ['welcome', 'to', 'the', 'jungle']

txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)   # ['hello', 'my name is Peter', 'I am 26 years old']

txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)    # ['apple', 'banana', 'cherry', 'orange']

txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)    # ['apple', 'banana#cherry#orange']

# ============================================================================================


# .strip() :

#   - Remove spaces at the beginning and at the end of the string:
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite") # of all fruits banana is my favorite

txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")
print(x)    # banana


# ============================================================================================


# Case Changing of Python String Methods :
name = "Gufran"

#   - lower(): Converts all uppercase characters in a string into lowercase
print(name.lower()) # gufran

#   - upper(): Converts all lowercase characters in a string into uppercase
print(name.upper()) # GUFRAN

#   - title(): Convert string to title case
print(name.title()) # Gufran

#   - swapcase(): Swap the cases of all characters in a string
print(name.swapcase())  # gUFRAN

#   - capitalize(): Convert the first character of a string to uppercase
print(name.capitalize())  # Gufran

# there are many string methods to explore :

s = 'hi'
print(s[1])          ## i
print(len(s))        ## 2
print(s + ' there')  ## hi there


# ============================================================================================


# Concatenation :
#   - refers to the process of joining two or more strings together to create a new, single string

pi = 3.14
##text = 'The value of pi is ' + pi      ## NO, does not work, because you can't concat string with number
# for concat
text = 'The value of pi is '  + str(pi)  ## yes

# ============================================================================================


# String formatting
value = 2.791514
print(f'approximate value = {value:.2f}')  # approximate value = 2.79

car = {'tires':4, 'doors':2}
print(f'car = {car}') # car = {'tires': 4, 'doors': 2}


