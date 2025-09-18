# Question 1:  Define a class node to describe a singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Question 2:  Define a class SLL to implement singly linked list with __init__() method to create and initialize the start reference value.
class SLL:
    def __init__(self,start=None):
        self.start = start

# Question 3:  Define a method method is_empty()  to check if the linked list is empty in SLL class.
    def is_empty(self):
        return self.start is None # OR: return self.start == None 
    
# Question 4:  In class SLL, define a method insert_at_start() to insert an element at the starting of the list.  
def insert_at_start(self,data):
        new_node = Node(data,self.start)
        self.start = new_node
    
# Question 5:  In class SLL, define a method insert_at_last() to insert an element at the end of the list.  
