# Question:1
''' Define the Python class Person with instance object variables name and age. Set instance object variables in __init__() method. Also define show() method to display name and age of a person.'''

class Person:
    def __init__(self, name, age):
        # instance object variables
        self.name = name
        self.age = age

    def show(self):
        # method to display instance variables
        print(f"My name is {self.name} and I am {self.age} years old.")


# Example usage
p1 = Person("Alice", 25)
p1.show()   # Output: Name: Alice, Age: 25