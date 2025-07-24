class Node:
    data = None
    next = None
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return ("the nodedata is %s" % self.data)


class Linkedlist:

    def __init__(self):
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
        return " -> ".join(nodes)
    
    def add_to_tail(self, new_data):
        new_node = Node(new_data)
        current_node = self.head
        if not current_node:
            self.head = new_node
        else:
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node




l=Linkedlist()
l.add_to_head(10)
l.add_to_head(20)
l.add_to_head(30)
l.add_to_tail(40)
print(l)