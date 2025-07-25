import random

class Heap: 

    """
    min-heap, a balanced, complete binary tree. Perant < childs. Used in priority queue and heapsort.
    Not a binary search tree (BST), which has a global order, and locally left child < parent< right child. Used in binary search.
    """
    items = None # show the items in the heap, though not really needed, because the initialisation is done in __init__

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
            tree = list[list[int]]() # create a list, whose elements are list of integers
            for i in range(self.count_layer()-1): # from top to the second last layer
                tree.append(self.items[2**i-1:2**(i+1)-1])
            tree.append(self.items[2**(i+1)-1::]) # the last layer
            return '\n'.join(str(tree[i]) for i in range(len(tree)))
        
    def sift_down(self, index): # index starts from 0
        if index < 0 or index >= len(self.items):
            return 'Index out of bounds'
        elif 2*index+1 >= len(self.items):
            return
        elif 2*index+1 == len(self.items)-1:
            if self.items[index] > self.items[2*index+1]:
                self.items[index], self.items[2*index+1] = self.items[2*index+1], self.items[index]
            return
        else:
            if self.items[index] <= min(self.items[2*index+1], self.items[2*index+2]): # swap with the smaller child
                return
            elif self.items[index] > min(self.items[2*index+1], self.items[2*index+2]) and self.items[2*index+1] <= self.items[2*index+2]:
                self.items[index], self.items[2*index+1] = self.items[2*index+1], self.items[index]
                index = 2*index+1
                self.sift_down(index)
                return
            else:
                self.items[index], self.items[2*index+2] = self.items[2*index+2], self.items[index]
                index = 2*index+2
                self.sift_down(index) # Recursively sift down, write it as an 'external' function, with the class name 'self' apecified, and no 'self'in the parameter.                            
                return
            
    def sift_down_until(self, index, last): # index starts from 0, sift down until the item with index [last] (included)
        if index < 0 or index >= len(self.items):
            return 'Index out of bounds'
        elif 2*index+1 > last:
            return
        elif 2*index+1 == last:
            if self.items[index] > self.items[2*index+1]:
                self.items[index], self.items[2*index+1] = self.items[2*index+1], self.items[index]
            return
        else:
            if self.items[index] <= min(self.items[2*index+1], self.items[2*index+2]): # swap with the smaller child
                return
            elif self.items[index] > min(self.items[2*index+1], self.items[2*index+2]) and self.items[2*index+1] <= self.items[2*index+2]:
                self.items[index], self.items[2*index+1] = self.items[2*index+1], self.items[index]
                index = 2*index+1
                self.sift_down_until(index, last)
                return
            else:
                self.items[index], self.items[2*index+2] = self.items[2*index+2], self.items[index]
                index = 2*index+2
                self.sift_down_until(index, last) # Recursively sift down, write it as an 'external' function, with the class name 'self' apecified, and no 'self'in the parameter.                            
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
        
    def insert(self, data):
        self.items.append(data)
        self.sift_up(len(self.items)-1)
        return # return empty, because the items are already updated in self.items. in this way cannot use print to 'print the result of the function', because what gets printed is the return value, which is None.

    def remove_by_index(self, index): # switch with the last leaf on the tree, and pop that out
        if index < 0 or index >= len(self.items):
            return print('Index out of bounds')
        else:
            self.items[index], self.items[-1] = self.items[-1], self.items[index]
            self.items.pop()
            self.sift_down(index)
        return
    
    def remove_by_value(self, value):
        if self.is_empty():
            return 'The heap is empty'
        elif value not in self.items:
            return 'Value %s not found in the heap' % value
        else:
            index = self.items.index(value)
            self.remove_by_index(index)
        return
    
    def update_by_index(self, index, data):
        if index < 0 or index >= len(self.items):
            return print('Index out of bounds')
        else:
            self.items[index] = data
            self.sift_up(index)
            self.sift_down(index)
        return
        
    def update_by_value(self, value, new_value):
        if self.is_empty():
            return 'The heap is empty'
        elif value not in self.items:
            return 'Value %s not found in the heap' % value
        else:
            index = self.items.index(value)
            self.update_by_index(index, new_value)
        return

    def heapify(self): # Big O(n) time complexity, because the sift_down is called for each parent node, not for each leaf node.
        if self.is_empty():
            return 'The heap is empty'
        for i in range((len(self.items)-2)//2, -1, -1): # Start from the last parent node (calculated by the last child, the end of the list) and sift down. The -1 in the middle is to include 0.
            self.sift_down(i)
        return

    def heap_sort(self):
        if self.is_empty():
            return 'The heap is empty'
        else:
            self.heapify()
            for i in range(1, len(self.items)):
                self.items[0], self.items[-i] = self.items[-i], self.items[0]
                self.sift_down_until(0, len(self.items)-1-i) # sift down exludes the swapped items at thh end of the list             
            return self.items

myheap = Heap()
for i in random.sample(range(0,100),15):
    myheap.items.append(i)
print(myheap, '\n')    
myheap.heapify()
print(myheap, '\n')
sorted_list = myheap.heap_sort()
print(sorted_list, '\n')