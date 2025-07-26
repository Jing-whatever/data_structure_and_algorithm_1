import random

def bagosort(list):
    if len(list) == 0:
        print('List is empty.')
    while list != sorted(list): # sorted(list) returns a boolean value to indicate the list is sorted or not
        random.shuffle(list) # randonly rearrange the list
    return list

def selection_sort(list): # selection sort on the location, each time throw the min_value to the end of the list, and shorten the dearch length by 1. O(n**2) time complexity, and O(1) space.
    if len(list) == 0:
        print('List is empty.')
    else:
       for i in range(len(list)):
            max_index = 0
            max_value = list[0]
            for j in range(len(list)-i): 
                if list[j] > max_value:
                    max_value = list[j]
                    max_index = j
                j += 1
            list[max_index], list[len(list)-i-1] = list[len(list)-i-1], list[max_index]
    return

def quick_sort(mylist):
    if len(mylist) == 0:
        return 'List is empty.'
    elif len(mylist) == 1:
        return 'List has only one element.'
    else:
        while len(mylist) > 1:
            pivot = mylist[0]
            left = list()
            right = list()
            for i in range(1, len(mylist)):
                if mylist[i] <= pivot: 
                    left.append(mylist[i])
                    right.append(mylist[i])
            print(left)
            print(right)
        return quick_sort(left) + [pivot] + quick_sort(right) # Return a list. To change pivot into a list, just use [].
        




mylist = random.sample(range(1,100),5)
print(mylist)
mylist = quick_sort(mylist) # If writing 'mylist = selection_sort(mylist), then mylist would be None, because the return of the function is void.
print(mylist)

