# Searched Lists.

'''We know that searching lists usually takes linear time, but what if the list is sorted? 
In class, we discussed how we could find an item in a sorted list in log(n) time using a binary search. 
Implement this idea in a python function search_sorted_list(sorted_list,item) that determines if item is in
sorted_list in log(n) time using a binary search algorithm. Your function should be recursive, 
and should keep passing the whole list to itself (with other appropriate information), since if you keep taking slices,
you add the time of copying the list slices and end up with an O(n) algorithm.'''

'''def f(x,y, counter = 3):
   if x==0 or y == 0:
      return True
   print(x)
   print(y)
   f(x-1, y-1, counter=2)

f(5,4)'''

#1
def search_sorted_list(sorted_list, item, start=0, end=None):
    if end is None:
        end = len(sorted_list) - 1
    
    if start > end:
        return False  # Return false if length of list -1 < 0
    
    mid = (start + end) // 2
    print(mid)
    mid_item = sorted_list[mid]
    
    if item == mid_item:
        return True  # Base case: item found
    elif item < mid_item:
        return search_sorted_list(sorted_list, item, start, mid - 1)  # Search left half
    else:
        return search_sorted_list(sorted_list, item, mid + 1, end)  # Search right half

sorted_list = [1, 3, 4, 5, 6, 7, 8, 10, 11, 14, 20]
print(search_sorted_list(sorted_list, 8))  # Output: True
print(search_sorted_list(sorted_list, 9))  # Output: False


'''Even if our list is sorted, this still doesn’t give us the constant time searching behavior that we see in dictionaries. 
To achieve this, we use a Hash Table. Here’s how it works:
• First, we create an empty list that is much larger than the number of things we expect to put in it. We refer to each spot in the list as a slot.
• We create a hash function that tells us which slot any input of a given type should go into. 
For example, if our inputs are numbers and our list is of length l,
we could create a function that says that the number n should go into slot s, where s is the remainder when n is divided by l.
• Each new item goes into the slot given by the hash function. But what if the slot is already full? This is called a collision. 
There are various ways we could deal with this. One of the easiest is just to put the item in the next empty slot. 
This is known as “rehashing by linear probing.”
• We look up an item using the same methods we used to decide where to put it in the first place. 
First we look for it where the hash function says it should go, then if there is something else there,
we need to keep looking for it until we either find it or we find an open slot that means it isn’t there.
Create a HashList class in python that implements these ideas. You can assume that inputs will be integers. It should contain the following methods:
- HashList(length) creates a new empty HashList of the given length. hashfunction(item) tells you which slot the item is assigned to.
- put(item) adds the given item to the list. If the list is full, it throws an error.
- contains(item) returns True if the given item is in the list, and False otherwise. 
Make sure your method still works in the extreme case in which the list is entirely full and the given item isn’t in the list.
- items() returns a list of all items in the HashList. '''

#2
class HashList:
    def __init__(self, sizeHash):
        self.size = sizeHash
        # Initialize arrays w/ None
        self.slots = [None] * self.size
        self.data = [None] * self.size

    # changes the size of the HashList
    def HashList(self,length):
        self.size = length

    # index calc for each item
    def hashfunction(self,item,size):
        return item%size

    # inserts item into HashList
    # Best Case: O(1) - Inserting into an empty slot
    # Worst Case: O(n) - Linear probing when all slots are occupied
    def put(self,item):
        hashvalue = self.hashfunction(item, len(self.slots))
        # if the slot is empty the item is inserted into hashvalue index
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = item
            self.data[hashvalue] = item  
        # if the slot is unavailable the next available slot is found
        else:
            nextslot = (hashvalue + 1) % len(self.slots)
            while self.slots[nextslot] is not None and nextslot != hashvalue:
                nextslot = (nextslot + 1) % len(self.slots)
        # error if all slots are filled
            if nextslot == hashvalue:
                raise ValueError('List is Full')
            self.slots[nextslot] = item
            self.data[nextslot] = item         
   
    # checks if HashList contains an item
    # Best Case: O(1) - Item found at initial hashvalue index
    # Worst Case: O(n) - Item not found and needs linear probing through all slots
    def contains(self, item, startslot=None):
        if startslot is None:
            startslot = self.hashfunction(item,len(self.slots))
        # if item is found True is returned, if item isn't found False is returned 
        if self.slots[startslot] == item:
            return True
        elif self.slots[startslot] is None:
            return False
        # if item isn't at startslot continue to search, False is returned if not found
        else:
            nextslot = (startslot + 1) % len(self.slots)
            while self.slots[nextslot] is not None and nextslot != startslot:
                if self.slots[nextslot] == item:
                    return True
                nextslot = (nextslot + 1) % len(self.slots)
            return False
    
    # method to put all items in a list and return the list
    # Time Complexity: O(n) - Need to iterate through all slots
    def items(self):
        items = []
        for slot in self.slots:
            if slot is not None:
                items.append(slot)
        return items

   
h = HashList(10)
h.put(12)
h.put(13)
h.put(24)
h.put(2)
h.put(4)
h.put(5)
print(h.items())
print(h.contains(2))
print(h.contains(20))

#3
'''
In a comment, explain the running times of the HashList methods in the best-case scenario in which there are no collisions,
and in the worst-case scenario in which there are many collisions.

Scenario without collisions:
- The 'put' method will have a time complexity of O(1) since it'll calculate the hash value 
and insert the item into an empty slot directly without any more iterations.
- The 'contains' method have a time complexity of O(1) because it will directly find the item corresponding to its hash value without any need for probing.

Scenario with collisions:
- The 'put' method will have a time complexity of O(n) since it'll have to test through the hash table to find an empty slot,
 and in the worst case, it might need to iterate through all slots before finding an empty one.
- The 'contains' method will have a time complexity of O(n) since it'll have to test through the hash table to find the item,
 and for the worst case, it might have to iterate through the slots before finding the item or discovering it's not in the list.
'''

#4
'''
Also explain how we would have to modify things to convert our HashList into a dictionary.

I would modify the HashList into a dictionary by replacing the data lists and slots to store key-value pairs, 
and adjust the 'put' method to handle the pairs. The 'contains' method would have to search for keys versus items.

'''