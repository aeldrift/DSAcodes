# Node: In py, we make s class for node
# Example:
''' 
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
# Now we have: 10 -> 20 -> 30 -> None '''

# Operations on SLL:
# Insertion:
# At start:
def insert_at_start(self, data):
    self.head = Node(data, self.head)