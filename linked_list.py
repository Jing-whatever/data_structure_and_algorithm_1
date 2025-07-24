class Node:
    data = None
    next = None
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return ("the nodedata is %s" % self.data)


class Linkedlist:

    def __init__(self): # initialise an empty linked list
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def size(self):
        current_node = self.head
        size = 0
        while current_node:
            size += 1
            current_node = current_node.next
        return size
    
    def add_to_head(self, new_data):
        new_node = Node(new_data)       
        new_node.next = self.head
        self.head = new_node

    def __repr__(self):  # the form of the representation of the linked list
        nodes = []
        current_node = self.head
        while current_node:
            if current_node is self.head:
                nodes.append("[Head: %s]" % current_node.data)
            elif current_node.next is None:
                nodes.append("[Tail: %s]" % current_node.data)
            else:
                nodes.append("[%s]" % current_node.data)
            current_node = current_node.next
        return " -> ".join(nodes) # use a string-formed symbol to join the items in the list
    
    def add_to_tail(self, new_data):
        new_node = Node(new_data)
        current_node = self.head
        if not current_node:
            self.head = new_node
        else:
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def get_index(self, value):
        if self.is_empty():
            return "List is empty"
        else:
            current_node = self.head
            index = 0
            while current_node:
                if current_node.data == value:
                    return index
                else:
                    current_node = current_node.next
                    index += 1
            return "Value %s not found in the list" %value
        
    def get_value(self, index): # get data by index
        if self.is_empty():
            return "List is empty"
        elif index < 0:
            return "Index smaller than 0"
        elif index >= self.size():
            return "Index out of bounds"
        elif index == 0:
            return self.head.data
        else:
            current_node = self.head
            while index > 0:
                current_node = current_node.next
                index -= 1
            return current_node.data
        
    def remove_by_index(self, index):
        if self.is_empty():
            return "List is empty"
        elif index < 0:
            return "Index smaller than 0"
        elif index >= self.size():
            return "Index out of bounds"
        else:
            if index == 0:
                self.head = None
            else:
                current_node = self.head
                previous_node = None
                copy_index = index
                while copy_index > 0:
                    previous_node = current_node
                    current_node = current_node.next
                    copy_index -= 1
                previous_node.next = current_node.next
            return "Node at index %s removed" % index
        
    def remove_by_value(self, value):
        if self.is_empty():
            return "List is empty"
        elif self.head.data == value:
            new_head = self.head.next # "self.head = self.head.next" doesn't work, because self.head is not like current_node, which is a local variable?
            self.head = new_head
            return "The head node with value %s removed from the list" % value
        else:
            current_node = self.head
            previous_node = None
            while current_node:
                if current_node.data == value:
                    previous_node.next = current_node.next
                    return "Value %s removed from the list" % value
                else:
                    previous_node = current_node
                    current_node = current_node.next
            return "Value %s not found in the list" % value

    def insert_by_index(self, index, data): # the data is inserted at the index position
        if index < 0:
            return "Index smaller than 0"
        elif index >= self.size():
            return "Index out of bounds"
        elif index == 0:
            new_head = Node(data)
            new_head.next = self.head
            self.head = new_head
            return "Data %s inserted at the head" % (data)
        else:
            new_node = Node(data)
            previous_node = None
            current_node = self.head
            while index > 0:
                previous_node = current_node
                current_node = current_node.next
                index -= 1
            previous_node.next = new_node
            new_node.next = current_node
        return "Data %s inserted at the index %s" % (data, index)
    
    def insert_by_value(self, value, data): # the data is inserted after the first occurrence of value
        if self.is_empty():
            return "List is empty"
        else:
            current_node = self.head
            new_node = Node(data)
            while current_node:
                if current_node.data == value:
                    new_node.next = current_node.next
                    current_node.next = new_node
                    return "Data %s inserted after value %s" % (data, value)
                else:
                    current_node = current_node.next
            return "Value %s not found in the list" %value


        

l=Linkedlist()
for i in range(2,10,2): l.add_to_head(i)
for i in range(30,20,-2): l.add_to_tail(i)
print(l)
print(l.insert_by_value(24,100))
print(l)