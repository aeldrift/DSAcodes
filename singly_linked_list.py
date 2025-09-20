# Node: In py, we make s class for node
# Example:

class Node:
    def __init__(self, data):
        self.data = data    # store value
        self.next = None    # store reference to next node

# nodes created:
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

# Link them
n1.next = n2
n2.next = n3 
# Now we have: 10 -> 20 -> 30 -> None

# Operations on SLL:
# Insertion:
# At start:
def insert_at_start(self, data):
    self.head = Node(data, self.head)

# At last:
def insert_at_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node  # If list is empty
            return
        temp = self.head
        while temp.next:
            temp = temp.next     # Traverse to last node
        temp.next = new_node
# Deletion:
# At start:
def delete_at_start(self):
        if self.is_empty():
            print("List is empty. Nothing to delete.")
        else:
            self.head = self.head.next  # Move head to next node
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

