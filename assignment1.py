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

# Question:3 
''' Write a Python script to calculate average of elements of list. '''

numbers = [1, 2, 3, 4, 5]
print("Given list:", numbers)

if len(numbers) > 0:  # avoid ZeroDivisionError
    average = sum(numbers) / len(numbers)
    print("Average of elements:", average)
else:
    print("List is empty, cannot calculate average.")

# using Statistics built-in library:

import statistics

numbers = [10, 20, 30, 40, 50]

average = statistics.mean(numbers)
print("Average of elements:", average) 
# Output: Average of elements: 30

# Using numpy:

import numpy as np

numbers = [10, 20, 30, 40, 50]

average = np.mean(numbers)
print("Average of elements:", average)
# Output :Average of elements: 30.0

# Question:4
''' Write a Python script to create a list of first and terms of Fibonacci series.'''

n = int(input("How many fibonacci numbers? \n", ))

a, b = 0, 1
fib_series = []

for _ in range(n):
    fib_series.append(a)
    a, b = b, a + b

print("fibonacci series upto",n,"is:", fib_series)


# Question:5
'''Write a Python script to create a list of first and prime numbers.'''

N = 10
