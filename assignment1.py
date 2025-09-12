# question1: 
''' Give an array with some int type write a py script to sort array values.'''

import array as arr

a = arr.array('i',[9,20,13,4])
print(a)
print(type(a))

list=a.tolist()
print(list)
print(type(list)) # None
print("sorted list is:",sorted(list)) # [4,9,13,20]

# Question:2
''' Given a list of heterogeneous elements, write a py script to remove all the non int values from list. '''

# given list
list = [1, "hello", 3.14, 5, True, "42"]
print("Given list is:",list)

# new list with only integers (excluding bools)
list1 = []
for value in list:
    if isinstance(value, int) and not isinstance(value, bool):
        list1.append(value)

print("Filtered list (only integers):",list1)
# Output: 
# Given list is: [1, 'hello', 3.14, 5, True, '42']
# Filtered list (only integers): [1, 5]
