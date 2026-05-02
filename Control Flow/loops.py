# Loops or Iteration Statements

# Most of the processes require a group of instructions to be repeatedly executed.
# 
#  In programming terminology, it is called a loop. 
# Instead of the next step, if the flow is redirected towards any earlier step, it constitutes a loop.

# ============================================================================================

# for Loop :
#   - The for loop iterates over the items of any sequence, such as a list, tuple or a string .

words = ["one", "two", "three"]
for x in words:
    print(x)


# ============================================================================================

# while Loop :
#   - The while loop repeatedly executes a target statement as long as a given boolean expression is true.

i = 1
while i < 6:
    print(i)
    i += 1

# ============================================================================================


# Jump Statements :
#   - The jump statements are used to jump on a specific statement by breaking the current flow of the program. 
#   - In Python, there are two jump statements 
#       1. break 
#       2. continue.


# break :
x = 0
while x < 10:
    print("x: ", x)
    if x == 5:
        print("Breaking...")
        break
    x += 1

print("End")


# continue :
for letter in "Python":
    # continue when letter is 'h'
    if letter == 'h':
        continue
    print("Current Letter :", letter)


# ============================================================================================
