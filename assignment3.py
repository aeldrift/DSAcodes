# Question 1:  Define a class node to describe a singly linked list
class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

# Question 2:  Define a class SLL to implement singly linked list with __init__() method to create and initialize the start reference value.
class SLL:
    def __init__(self):
        self.start = None

# Question 3:  Define a method method is_empty()  to check if the linked list is empty in SLL class.
    def is_empty(self):
        return self.start is None

# Question 4:  In class SLL, define a method insert_at_start() to insert an element at the starting of the list.  
    def insert_at_start(self, data):
        new_node = Node(data, self.start)  # new node points to current start
        self.start = new_node              # update start to new node

# Question 5:  In class SLL, define a method insert_at_last() to insert an element at the end of the list.  

    def insert_at_last(self, data):
        new_node = Node(data)
        if self.is_empty():               
            self.start = new_node          # new node becomes the head
        else:
            temp = self.start
            while temp.next is not None:   # Traverse to the last node
                temp = temp.next
            temp.next = new_node           # Link last node to new node
            
# Question 6:  In class SLL, define a method insert_after() to insert an element after a specific index or value of the list.  
            
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("The given node cannot be None")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

# Extra: Search for a node by value
    def search(self, key):
        temp = self.start
        while temp:
            if temp.data == key:
                return temp
            temp = temp.next
        return None
# Question 7:  In class SLL, define a method  to print all the elements of the list.  
# Method defines: Print list
    def print_list(self):
        temp = self.start
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage
# instance of SLL
my_list = SLL()

# Insert elements
my_list.insert_at_start(10)              # List: 10
my_list.insert_at_start(20)              # List: 20 -> 10
my_list.insert_at_last(30)               # List: 20 -> 10 -> 30
my_list.insert_after(my_list.search(20), 25)  # List: 20 -> 25 -> 10 -> 30

# Print the list
my_list.print_list()

# Question 8:  In class SLL, define a method delete() to delete an element from the start.

# At start:
def delete_at_start(self):
        if self.is_empty():
            print("List is empty. Nothing to delete.")
        else:
            self.head = self.head.next  # Move head to next node

# Question 9:  In class SLL, define a method delete() to delete an element from the last

# At last:
def delete_at_end(self):
        if self.is_empty():
            print("List is empty. Nothing to delete.")
        elif self.head.next is None:
            self.head = None  # Only one node
        else:
            temp = self.head
            while temp.next.next:  # Stop at second last node
                temp = temp.next
            temp.next = None  # Remove reference to last node

# Question 10:  In class SLL, define a method deleye() to delete an element after a specific index or value of the list. 