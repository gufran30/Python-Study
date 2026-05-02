# List Comprehension in Python :

#   - A list comprehension is a concise way to create lists.

# It is used to define a list based on an existing iterable object, 
# such as a 
#   - list, 
#   - tuple, 
#   - or string, 
#   - and apply an expression to each element in the iterable.

# ====================================================================================

# The basic syntax of list comprehension is −
# new_list = [expression for item in iterable if condition]

# - "expression" 
#       - is the operation or transformation to apply to each item in the iterable.

# - "item" 
#       - is the variable representing each element in the iterable.

# - "iterable" 
#       - is the sequence of elements to iterate over.

# - "condition" (optional) 
#       - is an expression that filters elements based on a specified condition.

# ====================================================================================

# example :

# Suppose we want to convert all the letters in the string "hello world" to their upper-case form. Using list comprehension, we iterate through each character, check if it is a letter, and if so, convert it to uppercase, resulting in a list of uppercase letters −

string = "hello world"
uppercase_letters = [ char.upper() for char in string if char.isalpha()]

# output : ['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']


# ====================================================================================

# List Comprehensions and Lambda :
#   - In Python, lambda is a keyword used to create anonymous functions.
#   - An anonymous function is a function defined without a name

# We can use list comprehension with lambda by applying the lambda function to each element of an iterable within the comprehension, generating a new list.

# example :

# In the following example, we are using list comprehension with a lambda function to double each element in a given list "original_list". We iterate over each element in the "original_list" and apply the lambda function to double it −

original_list = [1, 2, 3, 4, 5]
doubled_list = [ (lambda x: x*2) (x) for x in original_list ]
print(doubled_list) # [2, 4, 6, 8, 10]

# you can use this instead of using lambda : 
#   doubled_list = [ x * 2 for x in original_list ]

# While using (lambda x: expression)(x) inside a list comprehension is technically valid, it is usually considered redundant in Python. You can achieve the exact same result more cleanly by putting the expression directly in the comprehension


# ====================================================================================

# Nested Loops in Python List Comprehension
list1=[1,2,3]
list2=[4,5,6]
CombList = [(x, y) for x in list1 for y in list2]
print(CombList)
# output - [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]


# ====================================================================================


# Conditionals in Python List Comprehension

listt = [ x for x in range(1, 21) if x%2==0]
print(listt)        # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# ====================================================================================

# List Comprehensions vs For Loop :
# List comprehensions are often preferred for simpler operations, while for loops offer more flexibility for complex tasks.

# EXAMPLE - Suppose we want to separate each letter in a string and put all non-vowel letters in a list object. We can do it by a for loop as shown below −

# Example Using For Loop
chars = []
for ch in "Deadpoetsociety":
    if ch not in "aeiou":
        chars.append(ch)
print(chars)    # ['D', 'd', 'p', 't', 's', 'c', 't', 'y']

# Example Using List Comprehension
chars = [ char for char in "Deadpoetsociety" if char not in "aeiou"]
print(chars)    # ['D', 'd', 'p', 't', 's', 'c', 't', 'y']


# =======================================================================================

# The following example uses list comprehension to build a list of squares of numbers between 1 to 10 −

squares = [x*x for x in range(1, 11)]
print(squares)


# =======================================================================================

# Advantages of List Comprehension
#   - Conciseness :
#       - List comprehensions are more concise and readable compared to traditional for loops, allowing you to create lists with less code.

#   - Efficiency :
#       - List comprehensions are generally faster and more efficient than for loops because they are optimized internally by Python's interpreter.

#   - Clarity :
#       -  List comprehensions result in clearer and more expressive code, making it easier to understand the purpose and logic of the operation being performed

#   - Reduced Chance of Errors :
#       - Since list comprehensions are more compact, there is less chance of errors compared to traditional for loops, reducing the likelihood of bugs in your code.