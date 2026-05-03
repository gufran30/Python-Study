# Python Data Structure
#   - DS are a way of organizing data 
#   - so that it can be accessed more efficiently depending upon the situation.
#   - following are the some python data structure :
#       - Lists
#       - Tuples
#       - Sets
#       - Dictionaries


# Lists :
#   - List is one of the built-in data types in Python. 
#   - A Python list is a sequence of comma separated items, enclosed in square brackets [ ]. 
#   - The items in a Python list need not be of the same data type.

# examples :
list1 = ["Rohan", "Physics", 21, 69.75]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = [25.50, True, -55, 1+2j]

print(list1) # ['Rohan', 'Physics', 21, 69.75]
print(list2) # [1, 2, 3, 4, 5]
print(list3) # ['a', 'b', 'c', 'd']
print(list4) # [25.5, True, -55, (1+2j)]

# - List is an ordered collection of items.
# - Each item in a list has a unique position index, starting from 0.
# - A list in Python is similar to an array in C, C++ or Java.
# - However, the major difference is that in C/C++/Java, the array elements must be of same type. 
#       - On the other hand, Python lists may have objects of different data types.

# note :
#   - A Python list is mutable. Any item from the list can be accessed using its index, and can be modified.
#   - One or more objects from the list can be removed or added
#   - A list may have same item at more than one index positions. (means duplicate elements are allowed)

# ===============================================================================================

# Accessing Values in Lists
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];

print ("list1[0]: ", list1[0])  # list1[0]:  physics
print ("list2[1:5]: ", list2[1:5])  # list2[1:5]:  [2, 3, 4, 5]


# Updating Lists
listt = ['physics', 'chemistry', 1997, 2000];
print ("Value available at index 2 : ")
print (listt[2]) # 1997

listt[2] = 2001;
print ("New value available at index 2 : ")
print (listt[2]) # 2001

# Delete List Elements
list1 = ['physics', 'chemistry', 1997, 2000];
print (list1)   # ['physics', 'chemistry', 1997, 2000]
del list1[2];
print ("After deleting value at index 2 : ")
print (list1)   # ['physics', 'chemistry', 2000]
list1.remove(2000)
print(list1)    # ['physics', 'chemistry']

# ===============================================================================================

# Python List Operations
# - In Python, List is a sequence. 
# - Hence, we can concatenate two lists with "+" operator 
# - and concatenate multiple copies of a list with "*" operator.
# - The membership operators "in" and "not in" work with list object.

# concatenation
print([1, 2, 3] + [4, 5, 6]) # [1, 2, 3, 4, 5, 6]

# Repetition
print(['Hi!'] * 4)  # ['Hi!', 'Hi!', 'Hi!', 'Hi!']

# Membership
print(3 in [1, 2, 3])   # True

# ===============================================================================================

# Indexing, Slicing, and Matrixes
#   - Because lists are sequences, 
#       - indexing and slicing work the same way for lists as they do for strings.

L = ['spam', 'Spam', 'SPAM!']
print(L[2]) # SPAM!
print(L[-2])   # Spam 
print(L[1:])  # ['Spam', 'SPAM!']  


# ===============================================================================================

# Built-in Functions with Lists
# cmp(list1, list2) - no longer available, should use standard comparision operators 
list1 = [1, 2, 3]
list2 = [1, 2, 4]
print(list1 == list2)  # Returns False
print(list1 < list2)   # Returns True

# len(list)
list1 = [1, 2, 3]
print(len(list1))   # 3

# max(list)
list1 = [1, 4, 9, 2, 3]
print(max(list1))   # 9

# min(list)
list1 = [1, 4, 9, 2, 3]
print(max(list1))   # 1

# list(seq)
tupleDS = (123, 'xyz', 'zara', 'abc')
covertedIntoList = list(tupleDS)
print("List elements : ", covertedIntoList)



# ===============================================================================================

# Python List Methods : 

#  - list.append(obj) - Appends object obj to list.
aList = ['123', 'xyz', 'zara', 'abc'];
aList.append('2009');
print("Updated List : ", aList)


#  - list.clear()   - Clears the contents of list.
aList = ['123', 'xyz', 'zara', 'abc'];
print("Before clear : ", aList)
aList.clear()
print("After clear : ", aList)


#  - list.copy()    - Returns a copy of the list object.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#  - list.count(obj)   - Returns count of how many times obj occurs in list
aList = [123, 'xyz', 'zara', 'abc', 123]
print("Count for 123 : ", aList.count(123)) # Count for 123 :  2
print("Count for zara : ", aList.count('zara')) # Count for zara :  1


#  - list.extend(seq)   - Appends the contents of seq to list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)   # ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']


#  - list.index(obj)    - Returns the position at the first occurrence of the specified value.
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)     # 2


#  - list.insert(index, obj) - Inserts object obj into list at offset index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) # ['apple', 'orange', 'banana', 'cherry']


#  - list.pop(index) - The pop() method removes the element at the specified position.
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)   # ['apple', 'cherry']


#  - list.remove(obj)   - Removes object obj from list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # ['apple', 'cherry']

#  - list.reverse()     - Reverses objects of list in place
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)   # ['cherry', 'banana', 'apple']

#  - list.sort([func])  
#       - Sorts objects of list, use compare func if given
#       - The sort() method sorts the list ascending by default.
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars) # ['BMW', 'Ford', 'Volvo']

cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars) # ['Volvo', 'Ford', 'BMW']
