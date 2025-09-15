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
p1.show()   # Output: My name is Alice and I am 25 years old

# Question:2
''' Define class circle with instance object radius. Provide getter setter for radius also define getarea and getcurcuference methods.'''

import math

class Circle:
    def __init__(self, radius):
        self._radius = radius   # private variable

    # Getter
    @property
    def radius(self):
        return self._radius

    # Setter (with validation)
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    # Method to calculate area
    def get_area(self):
        return math.pi * (self._radius ** 2)

    # Method to calculate circumference
    def get_circumference(self):
        return 2 * math.pi * self._radius


c = Circle(5)
print("Radius:", c.radius)                 # getter
print("Area:", c.get_area())               # area = πr²
print("Circumference:", c.get_circumference())  # 2πr

c.radius = 10   # setter
print("New Radius:", c.radius)
print("New Area:", c.get_area())

