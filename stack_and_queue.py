class Stack:
    items = None

    def __init__(self):
        self.items = list[int]()
    
    def is_empty(self):
        return len(self.items) ==0
    
    def __repr__(self):
        if self.is_empty():
            return 'The stack is empty'
        else:
            return '->'.join(str(self.items[i]) for i in range(len(self.items)))
    
    def push(self, data):
        self.items.append(data)

    def popstack(self):
        if self.is_empty():
            return 'The stack is empty'
        else:
            data = self.items.pop()
            print('Data %s is poped from the stack' % data)

    def peek(self):
        if self.is_empty():
            return 'The stack is empty'
        else:
            return self.items[-1]

my_stack = Stack()
for i in range(30,50,4):
    my_stack.push(i)
print(my_stack.peek())
while not my_stack.is_empty():
    my_stack.popstack()
print(my_stack)


class Queue:
    items = None

    def __init__(self):
        self.items = list[int]()

    def is_empty(self):
        return len(self.items) == 0
    
    def __repr__(self):
        if self.is_empty():
            return 'The queue is empty'
        else:
            return '->'.join(str(self.items[i]) for i in range(len(self.items)))
    
    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if self.is_empty():
            return 'The queue is empty'
        else:
            data = self.items[0]
            self.items = self.items[1::]
            print('Data %s is dequeued' % data)

    def peek(self):
        if self.is_empty():
            return 'The queue is empty'
        else:
            return self.items[0]
        
my_queue = Queue()
for i in range(30,50,4):
    my_queue.enqueue(i)
print(my_queue)
print(my_queue.peek())
while not my_queue.is_empty():
    my_queue.dequeue()
print(my_queue)