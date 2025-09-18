# Question1:  Define a class node to describe a singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Question2:  Define a class SLL to implement singly linked list with __init__() method to create and initialize the start reference value.
class SLL:
    def __init__(self,start=None):
        self.start = start

# Question3:  Define a method method is_empty()  to check if the linked list is empty in SLL class.
    def is_empty(self):
        return self.start is None # OR: return self.start == None 