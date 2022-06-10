'''
UNORDERED LINKED LISTS

    -linear data structure in which data is stored contigously. 
    -each "link" consists of the data field, and a reference to the next node.
    -a reference "head" is used to refer to the first node of the list

    BASIC STRUCTURE: where x, y, z is the data, and r is the reference to the next node.

                 _________         _________         _________
    head -----> |__x_|__r_| ----> |__y_|__r_| ----> |_z__|__r_| -----> none  

'''

'''
NODE CLASS

    class used to create the node object.
    each object hold two pieces of information:
    
        -the data field (item itself)
        -reference to the next node

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
LINKED LIST CLASS (UNORDERED)

  METHODS

    1. is_empty():
        simply returns True if list is empty (if self.head == None)

    2. prepend(item):
        since this linked list is unordered, the location of the new node with respect
        to the nodes already in the list is not important, thus we can simply add the 
        new item to the first location of the list.

        -create a new node
        -link the new node to the first node of the list (using head)
        -set the head as the new node

    3. append(item):
        append means to add new node to the end of the list.
        this is the opposite of prepend, which adds node to the beginning of the list.

        -create a new node
        -create a reference (current), set as head
        if current is None (empty list):
            set head as new node
        else:
            while current.next is not None:
                set current as current.next
            point current.next to new node.        


    4. insert(item, index):
        inserts at a designated index.

        -create a new node
        -create a reference (current), set it as head
        -create a reference (previous), set it as None
        -create a var (reached), set it as False
        -create a var (count), set as 0
        -if current is None:
            set the head as the new node
        -else:
            -while reached is False:
                increment the count
                if count == the index:
                    reached = True
                else:
                    set previous as current
                    set current as current.next
            if count == 1:
                point the new node to the current
                set the head as the new node
            else:
                point the new node to the current
                point the previous node to the new node.            


    5. pop():
        removes item at the end of the list.

        -create a reference (current) that starts at the head of the node
        -create a reference (previous), which will be initialized to None
        -while current.next is not None (go until current is at last node)
            set previous to current
            set current to the next node
        -set previous.next to current.next (current will now be eliminated)

    6. remove(item):
        deletes a node that contains the item specified.

        -create a reference (current) that starts aht the head of the node
        -create a reference (previous), which will be initialized to None
        -create a var (found) and set it to False
        -while found is False:
            if current.data == item:
                set found to True
            else:
                set previous as current
                set current as current.next
        -if previous is None (means item is in the first node of the list (self.head))
            set the head as current.next
        -else:
            point previous.next to current.next  

    7. size()
        returns the size of the list.

        -create a reference (current) that starts at the head of the node, and a counter 
        -while current is not None (end of list):
            -increment counter
            -set current to the next node (.next)
        return counter   

    8. search(item):
        traverses through the list to find item.
        -create a reference (current) that starts at the head of the node
        -create a var (found) and initialize to False. If found, set it to True.
        -while found is False and current != None:
            -if current.data == item:
                set found to True
            -else:
                set current to the next node 
        return found 

    9. print_fn():
        output the linked list in array form.

        -create a reference (current) that starts at the head of the node
        -create a list that will hold the elements in the list
        -while current is not None (end of list):
            -add data of current node to the list
        -print the list    
'''

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def prepend(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def append(self, item):
        new_node = Node(item)
        current = self.head
        if current == None:
            self.head = new_node
        else:
            while current.next != None:
                current = current.next
            current.next = new_node        

    def insert(self, item, index):
        new_node = Node(item)
        current = self.head
        previous = None
        reached = False
        count = 0
        if current == None:
            self.head = new_node
        else:
            while reached == False:
                count += 1
                if count == index:
                    reached = True
                else:
                    previous = current
                    current = current.next              
            if count == 1: #if index is 1
                new_node.next = current
                self.head = new_node
            else:
                new_node.next = current
                previous.next = new_node    

    #must work on if there is only one node in the list.
    def pop(self):
        current = self.head
        previous = None
        while current.next != None:
            previous = current
            current = current.next
        previous.next = current.next
        
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while found == False:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next            

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count+=1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        found = False
        while found == False and current != None:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found

    def print_fn(self):
        current = self.head
        ll = []
        while current != None:
            ll.append(current.data)
            current = current.next
        return ll    
