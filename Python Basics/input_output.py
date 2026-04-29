# Input and Output in Python

# - The print() function is used for output in various formats.
# - The input() function enables interaction with users.

# ============================================================================================

# Taking Input from user using input()
name = input("Enter your name: ")   # ask user to type name
print("Hello,", name, "! Welcome!") 

# ============================================================================================

# Taking Different types of User Input
#  - We can change the user input from default string type to any other type (int, float, etc) by typecasting:

i = int(input("How old are you?: "))
f = float(input("Type 12 to get its float value: "))

print(i, f)


# ============================================================================================


# f-strings in Python :
#   - make string formatting and interpolation easier.
name = 'Gufran'
age = 22
print(f"Hello, My name is {name} and I'm {age} years old.")


# ============================================================================================


# Print date using f-string in Python
import datetime

today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")

# Formatting codes:
# %B → full month name
# %d → day of the month
# %Y → year

# ============================================================================================

english = 78
maths = 56
science = 85

print(f"Gufran got total marks {english + maths + science} out of 300")