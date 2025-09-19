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

# Print list
    def print_list(self):
        temp = self.start
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# -------------------------------
# Example usage
# -------------------------------
my_list = SLL()

# Insert nodes
my_list.insert_at_last(20)
my_list.insert_at_start(10)
my_list.insert_at_last(30)

print("Initial list:")
my_list.print_list()

# Insert after a specific node (search first)
node = my_list.search(20)
my_list.insert_after(node, 25)

print("\nAfter inserting 25 after 20:")
my_list.print_list()