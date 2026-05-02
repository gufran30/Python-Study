# Python program control flow is regulated by various types of 
#   - conditional statements, 
#   - loops, 
#   - and function calls. 
# 
# By default, the instructions in a computer program are executed in a sequential manner, from top to bottom, or from start to end. 
# 
# However, such sequentially executing programs can perform only simplistic tasks. 
# We would like the program to have a decision-making ability, so that it performs different steps depending on different conditions.

# The if Statements

marks = 80
result = ""
if marks < 30:
    result = "Failed"
elif marks > 75 :
    result = "Passed with distinction"
else:
    result = "Passed"

print(result)

# ============================================================================================


# The match Statement

def checkVowel(n):
    match n:
        case 'a' : return "Vowel alphabet"
        case 'e' : return "Vowel alphabet"
        case 'i' : return "Vowel alphabet"
        case 'o' : return "Vowel alphabet"
        case 'u' : return "Vowel alphabet"
        case _ : return "Simple alphabet"

print(checkVowel('a'))  # Vowel alphabet
print(checkVowel('m'))  # Simple alphabet
print(checkVowel('o'))  # Vowel alphabet