class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __repr__(self):
        return str(self.data)

class LinkedList():
    def __init__(self, data = None):
        self.head = data
    def add_first(self, data):
        self.head = data
    def add_last(self, data):
        self.head(data)
    def display(self):
        return print(self.head)


ll = LinkedList()
print("Empty Linked List: ", end= "")
ll.display()

ll.add_first(5)
print("Adding first: ", ll.display())

ll.add_first(8)
print("Adding first: ", ll.display())

ll.display()




