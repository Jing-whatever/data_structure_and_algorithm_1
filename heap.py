class Heap: 

    """
    min-heap, a balanced, complete binary tree. Perant < childs. Used in priority queue and heapsort.
    Not a binary search tree (BST), which has a global order, and locally left child < parent< right child. Used in binary search.
    """
    items = None # show the items in the heap

    def __init__(self):
        self.items = list[int]()

    def is_empty(self):
        return len(self.items) == 0
    
    def count_layer(self): # return the number of layers in the heap
        layers = 0
        while 2**layers-1 < len(self.items):
            layers += 1
        return layers
    
    def __repr__(self):
        if self.is_empty():
            return 'The heap is empty'
        elif self.count_layer == 1:
            return 'The heap has only one layer: %s' % self.items[0]
        else:
            tree = list[list[int]]()
            for i in range(self.count_layer()-1): # from top to the second last layer
                tree.append(self.items[2**i-1:2**(i+1)-1])
            tree.append(self.items[2**(i+1)-1::]) # the last layer
            return '\n'.join(str(tree[i]) for i in range(len(tree)))
        
    def sift_down(self, index):
        if index < 0 or index >= len(self.items):
            return 'Index out of bounds'
        elif 2*index+1 >= len(self.items):
            return
        elif 2*index+1 == len(self.items)-1:
            if self.items[index] > self.items[2*index+1]:
                self.items[index], self.items[2*index+1] = self.items[2*index+1], self.items[index]
            return
        else:
            if self.items[index] > self.items[2*index+1]:
                self.items[index], self.items[2*index+1] = self.items[2*index+1], self.items[index]
                index = 2*index+1
                self.sift_down(index) # recursively sift down, write it as an 'external' function, with the class name 'self' apecified, and no 'self'in the parameter 
            elif self.items[index] > self.items[2*index+2]:
                self.items[index], self.items[2*index+2] = self.items[2*index+2], self.items[index]
                index = 2*index+2
                self.sift_down(index)
            else:
                return
            
    def sift_up(self, index):
        if index < 0 or index >= len(self.items):
            return print('Index out of bounds')
        elif index == 0:
            return
        else:
            if self.items[index] < self.items[(index-1)//2]:
                self.items[index], self.items[(index-1)//2] = self.items[(index-1)//2], self.items[index]
                index = (index-1)//2
                self.sift_up(index)
            return
        
    def get_min(self):
        if self.is_empty():
            return 'The heap is empty'
        else:
            return self.items[0]

    def extract_min(self):
        if self.is_empty():
            return 'The heap is empty'
        else:
            min = self.items[0]
            self.items[0], self.items[-1] = self.items[-1], self.items[0]
            self.items.pop()
            self.sift_down(0)
            return min



heap = Heap()
for i in range(100,20,-10):
    heap.items.append(i)
print(heap, '\n')
heap.sift_up(6)
heap.sift_up(7)
print(heap, '\n')
print(heap.get_min())
print(heap.extract_min())
print(heap, '\n')