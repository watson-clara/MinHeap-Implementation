# Name: Clara  Watson
# OSU Email: watsoncl@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: min_heap.py
# Due Date: May 23, 2021


from ast import Not
from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        TODO: This method adds a new object to the MinHeap while maintaining heap property
        """
         #using the info from the exploration-heap-implementation page linked on assignment page
         #Put the new element at the end of the array.
        self._heap.append(node)
        #Compute the inserted element’s parent index, (i − 1) / 2.
        node_index = self.size() - 1
        #Compare the value of the inserted element with the value of its parent.
        parent_index = node_index 
        #If the value of the parent is greater than the value of the inserted element, 
        # swap the elements in the array and re
        while not parent_index == 0: 
            parent_index = (parent_index - 1) // 2
            parent = self._heap.get_at_index(parent_index)
            if parent > node:
                self._heap.set_at_index(node_index, parent)
                self._heap.set_at_index(parent_index, node)
                node_index = parent_index
        
        
    def is_empty(self) -> bool:
        """
        TODO: This method returns True if the heap is empty; otherwise, it returns False.
        """
        return self._heap.is_empty()


    def get_min(self) -> object:
        """
        TODO: This method returns an object with the minimum key, without removing it from the heap. If the heap is empty, the method raises a MinHeapException.
        """
        if self.is_empty():
            raise MinHeapException
        else: 
            return self._heap.get_at_index(0)


    def remove_min(self) -> object:
        """
        TODO: This method returns an object with the minimum key, and removes it from the heap. If the heap is empty, the method raises a MinHeapException.
        """
        #using the info from the exploration-heap-implementation page linked on assignment page
        if self.is_empty():
            raise MinHeapException
        #Remember the value of the first element in the array (to be returned later).
        first_element = self.get_min()
        #find last element 
        last_index = self.size() -1
        #Replace the value of the first element in the array with the value of the last element,    
        last_element = self._heap.get_at_index(last_index)
        self._heap.set_at_index(0, last_element)
        #and remove the last element.
        self._heap.remove_at_index(last_index)
        #If the array is not empty
        if self.is_empty():
            return first_element
        #compute the indices of the children of the replacement element (2 * i + 1 and 2 * i + 2).
        end = last_element
        current = 0 
        # and repeat from step 3.
        while current < self.size():
            left_child_index = current * 2+1
            right_child_index = current *2+2
            if left_child_index >= self.size():
                return first_element
            elif right_child_index == self.size():
                left_child = self._heap.get_at_index(left_child_index)
                if end >= left_child:
                    index1 = left_child_index
                    index2 = current
                    val1 = self._heap.get_at_index(index1)
                    val2 = self._heap.get_at_index(index2)
                    self._heap.set_at_index(index1, val2)
                    self._heap.set_at_index(index2, val1)
                    return first_element
                else: 
                    return first_element
            else: 
                pass
            left_child = self._heap.get_at_index(left_child_index)
            right_child = self._heap.get_at_index(right_child_index)
            if end < left_child:
                if last_element < right_child:
                    return first_element
                else: 
                    pass
            if left_child <= right_child:
                index1 = left_child_index
                index2 = current
                val1 = self._heap.get_at_index(index1)
                val2 = self._heap.get_at_index(index2)
                self._heap.set_at_index(index1, val2)
                self._heap.set_at_index(index2, val1)
                current = left_child_index
            else: 
                if end < right_child:
                    return first_element
                else:
                    index1 = right_child_index
                    index2 = current
                    val1 = self._heap.get_at_index(index1)
                    val2 = self._heap.get_at_index(index2)
                    self._heap.set_at_index(index1, val2)
                    self._heap.set_at_index(index2, val1)
                    current = right_child_index
        
            
            
            
    def build_heap(self, da: DynamicArray) -> None:
        """
        TODO: This method receives a Dynamic Array with objects in any order, and builds a proper MinHeap from them. 
        """
        #using the info from the exploration-heap-implementation page linked on assignment page
        #each individual leaf subtree is a proper heap (of one element).
        self.clear()
        for i in range(da.length()):
            self._heap.append(da[i])
        #The first non-leaf element (from the back of the array) is at n / 2 − 1
        #We can repeat this, moving backwards one element at a time from the first non-leaf element, 
        # and each time we percolate an element down, 
        # the subtree rooted at that element’s original position will be a proper heap.
        count = 0 
        while 2 ** count < self.size():
            current_index = (self.size() // 2) - 1
            while current_index >=0:
                left_child_index = current_index * 2+1
                right_child_index = current_index *2+2
                if right_child_index == self.size():
                    if self._heap.get_at_index(current_index) > self._heap.get_at_index(left_child_index):
                        index1 = current_index
                        index2 = left_child_index
                        val1 = self._heap.get_at_index(index1)
                        val2 = self._heap.get_at_index(index2)
                        self._heap.set_at_index(index1, val2)
                        self._heap.set_at_index(index2, val1)
                elif  self._heap.get_at_index(current_index) > self._heap.get_at_index(left_child_index) or self._heap.get_at_index(current_index) > self._heap.get_at_index(right_child_index):
                    if self._heap.get_at_index(left_child_index) > self._heap.get_at_index(right_child_index):
                        index1 = current_index
                        index2 = right_child_index
                        val1 = self._heap.get_at_index(index1)
                        val2 = self._heap.get_at_index(index2)
                        self._heap.set_at_index(index1, val2)
                        self._heap.set_at_index(index2, val1)
                    else:
                        index1 = current_index
                        index2 = left_child_index
                        val1 = self._heap.get_at_index(index1)
                        val2 = self._heap.get_at_index(index2)
                        self._heap.set_at_index(index1, val2)
                        self._heap.set_at_index(index2, val1)
                   
                current_index = current_index - 1
            count = count + 1
                
                
                
    def size(self) -> int:
        """
        TODO: This method returns the number of items currently stored in the heap.
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        TODO: This method clears the contents of the heap.
        """
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    TODO: receives a DynamicArray and sorts its content in non-ascending order using the Heapsort algorithm
    """
    
    length = da.length()
    count = length - 1
    counter = False
    heap = MinHeap()
    heap.build_heap(da)
    while count >= 0:
        da[count] = heap.remove_min()
        if counter is False: 
            count = count - 1

# It's highly recommended that you implement the following optional          #
# helper function for percolating elements down the MinHeap. You can call    #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    TODO: Write your implementation
    """
    pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
