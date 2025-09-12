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
