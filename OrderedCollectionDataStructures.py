# Question 1
class Stack:
    def __init__(self):
        """
        Constructor to create a new empty stack.
        Time complexity: O(1)
        """
        self.items = []

    def push(self, item):
        """
        Method to add a new item to the top of the stack.
        Time complexity: O(1)
        """
        self.items.append(item)

    def pop(self):
        """
        Method to remove the top item from the stack and return it.
        If the stack is empty, returns None.
        Time complexity: O(1)
        """
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        """
        Method to return the top item from the stack without removing it.
        If the stack is empty, returns None.
        Time complexity: O(1)
        """
        if self.isEmpty():
            return None
        return self.items[-1]

    def isEmpty(self):
        """
        Method to check if the stack is empty.
        Time complexity: O(1)
        """
        return len(self.items) == 0

    def size(self):
        """
        Method to return the size of the stack.
        Time complexity: O(1)
        """
        return len(self.items)


# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Size of stack:", stack.size())  # Output: 3
print("Top item:", stack.peek())  # Output: 3
print("Popped item:", stack.pop())  # Output: 3
print("Is stack empty?", stack.isEmpty())  # Output: False
print("Popped item:", stack.pop())  # Output: 2
print("Popped item:", stack.pop())  # Output: 1
print("Is stack empty?", stack.isEmpty())  # Output: True


class Queue:
    def __init__(self):
        """
        Constructor to create an empty queue.
        Time complexity: O(1)
        """
        self.items = []

    def enqueue(self, item):
        """
        Method to add a new item to the "bottom" of the queue.
        Time complexity: O(1)
        """
        self.items.append(item)

    def dequeue(self):
        """
        Method to remove the front item from the queue and return it.
        If the queue is empty, returns None.
        Time complexity: O(1) amortized time
        """
        if self.isEmpty():
            return None
        return self.items.pop(0)

    def isEmpty(self):
        """
        Method to check if the queue is empty.
        Time complexity: O(1)
        """
        return len(self.items) == 0

    def size(self):
        """
        Method to return the current number of items in the queue.
        Time complexity: O(1)
        """
        return len(self.items)


# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Size of queue:", queue.size())  # Output: 3
print("Front item:", queue.dequeue())  # Output: 1
print("Is queue empty?", queue.isEmpty())  # Output: False
print("Dequeued item:", queue.dequeue())  # Output: 2
print("Dequeued item:", queue.dequeue())  # Output: 3
print("Is queue empty?", queue.isEmpty())  # Output: True


class Deque:
    def __init__(self):
        """
        Constructor to create an empty deque.
        Time complexity: O(1)
        """
        self.items = []

    def addFront(self, item):
        """
        Method to add an item to the front of the deque.
        Time complexity: O(1)
        """
        self.items.insert(0, item)

    def addRear(self, item):
        """
        Method to add an item to the rear of the deque.
        Time complexity: O(1)
        """
        self.items.append(item)

    def removeFront(self):
        """
        Method to remove and return the front item from the deque.
        If the deque is empty, returns None.
        Time complexity: O(1)
        """
        if self.isEmpty():
            return None
        return self.items.pop(0)

    def removeRear(self):
        """
        Method to remove and return the rear item from the deque.
        If the deque is empty, returns None.
        Time complexity: O(1)
        """
        if self.isEmpty():
            return None
        return self.items.pop()

    def isEmpty(self):
        """
        Method to check if the deque is empty.
        Time complexity: O(1)
        """
        return len(self.items) == 0

    def size(self):
        """
        Method to return the current number of items in the deque.
        Time complexity: O(1)
        """
        return len(self.items)


# Example usage:
deque = Deque()
deque.addFront(1)
deque.addRear(2)
deque.addFront(3)

print("Size of deque:", deque.size())  # Output: 3
print("Front item:", deque.removeFront())  # Output: 3
print("Rear item:", deque.removeRear())  # Output: 2
print("Is deque empty?", deque.isEmpty())  # Output: False
print("Removed item:", deque.removeFront())  # Output: 1
print("Is deque empty?", deque.isEmpty())  # Output: True


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.isHead = False


class Linked_List:
    def __init__(self):
        """
        Constructor to create a new empty linked list.
        """
        self.head = None
        self.size = 0

    def add(self, item):
        """
        Method to add a new item to the beginning of the list.
        """
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def remove(self, item):
        """
        Method to remove the item from the list.
        """
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.item == item:
                found = True
            else:
                previous = current
                current = current.next
        if found:
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next
            self.size -= 1
        else:
            raise KeyError("Item not found in the list.")

    def search(self, item):
        """
        Method to search for the item in the list.
        """
        current = self.head
        while current:
            if current.item == item:
                return True
            current = current.next
        return False

    def isEmpty(self):
        """
        Method to check if the list is empty.
        """
        return self.size == 0

    def size(self):
        if self.headNode == None:
            return 0
        else: 
            node = self.headNode
            counter = 1
            while node.nextNode != None:
                node = node.nextNode
                counter += 1
            return counter

    def append(self, item):
        """
        Method to add a new item to the end of the list.
        """
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def index(self, item):
        """
        Method to return the position of item in the list.
        """
        current = self.head
        index = 0
        while current:
            if current.item == item:
                return index
            current = current.next
            index += 1
        raise KeyError("Item not found in the list.")

    def insert(self, position, item):
        """
        Method to add a new item to the list at position.
        """
        if position < 0 or position > self.size:
            raise ValueError("Invalid position.")
        if position == 0:
            self.add(item)
        else:
            new_node = Node(item)
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.size += 1

    def pop(self):
        """
        Method to remove and return the last item in the list.
        """
        if self.isEmpty():
            raise ValueError("List is empty.")
        current = self.head
        previous = None
        while current.next:
            previous = current
            current = current.next
        if previous is None:
            self.head = None
        else:
            previous.next = None
        self.size -= 1
        return current.item

    def pop(self, pos):
        """
        Method to remove and return the item at position pos.
        """
        if pos < 0 or pos >= self.size:
            raise ValueError("Invalid position.")
        if pos == 0:
            return self.pop()
        current = self.head
        previous = None
        for _ in range(pos):
            previous = current
            current = current.next
        previous.next = current.next
        self.size -= 1
        return current.item


# Example usage:
linked_list = Linked_List()
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)

print("Size of linked list:", linked_list.size())  # Output: 3
print("Search for item 2:", linked_list.search(2))  # Output: True
print("Search for item 4:", linked_list.search(4))  # Output: False

linked_list.remove(2)
print("Size of linked list after removing item 2:", linked_list.size())  # Output: 2

linked_list.append(4)
print("Size of linked list after appending item 4:", linked_list.size())  # Output: 3

print("Index of item 3:", linked_list.index(3))  # Output: 0
print("Index of item 4:", linked_list.index(4))  # Output: 2

linked_list.insert(1, 5)
print("Size of linked list after inserting item 5 at position 1:", linked_list.size())  # Output: 4

print("Popped item from end of linked list:", linked_list.pop())  # Output: 4
print("Size of linked list after popping from end:", linked_list.size())  # Output: 3

print("Popped item from position 1:", linked_list.pop(1))  # Output: 5
print("Size of linked list after popping from position 1:", linked_list.size())  # Output: 2


class Node:
    def __init__(self, item):
        self.item = item
        self.prev = None
        self.next = None


class DoubleLinked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def remove(self, item):
        current = self.head
        while current:
            if current.item == item:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                self.size -= 1
                return
            current = current.next
        raise KeyError("Item not found in the list.")

    def search(self, item):
        current = self.head
        while current:
            if current.item == item:
                return True
            current = current.next
        return False

    def isEmpty(self):
        return self.size == 0

    def size(self):
        return self.size

    def append(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def index(self, item):
        current = self.head
        index = 0
        while current:
            if current.item == item:
                return index
            current = current.next
            index += 1
        raise KeyError("Item not found in the list.")

    def insert(self, position, item):
        if position < 0 or position > self.size:
            raise ValueError("Invalid position.")
        if position == 0:
            self.add(item)
        elif position == self.size:
            self.append(item)
        else:
            new_node = Node(item)
            current = self.head
            for _ in range(position):
                current = current.next
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
            self.size += 1

    def pop(self):
        if self.isEmpty():
            raise ValueError("List is empty.")
        item = self.tail.item
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return item

    def pop(self, pos):
        if pos < 0 or pos >= self.size:
            raise ValueError("Invalid position.")
        if pos == 0:
            return self.pop()
        current = self.head
        for _ in range(pos):
            current = current.next
        item = current.item
        current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        self.size -= 1
        return item


# Example usage:
double_linked_list = DoubleLinked_List()
double_linked_list.add(1)
double_linked_list.add(2)
double_linked_list.add(3)

print("Size of doubly-linked list:", double_linked_list.size())  # Output: 3
print("Search for item 2:", double_linked_list.search(2))  # Output: True
print("Search for item 4:", double_linked_list.search(4))  # Output: False

double_linked_list.remove(2)
print("Size of doubly-linked list after removing item 2:", double_linked_list.size())  # Output: 2

double_linked_list.append(4)
print("Size of doubly-linked list after appending item 4:", double_linked_list.size())  # Output: 3

print("Index of item 3:", double_linked_list.index(3))  # Output: 0
print("Index of item 4:", double_linked_list.index(4))  # Output: 2

double_linked_list.insert(1, 5)
print("Size of doubly-linked list after inserting item 5 at position 1:", double_linked_list.size())  # Output: 4

print("Popped item from end of doubly-linked list:", double_linked_list.pop())  # Output: 4
print("Size of doubly-linked list after popping from end:", double_linked_list.size())  # Output: 3

print("Popped item from position 1:", double_linked_list.pop(1))  # Output: 5
print("Size of doubly-linked list after popping from position 1:", double_linked_list.size())  # Output: 2


# Python's internal representation of a list is not a linked-list or a doubly-linked list.
# Instead, it is implemented as a dynamic array, also known as a resizable array.
# Dynamic arrays offer constant-time random access, efficient memory allocation, and support for dynamic resizing.
# These characteristics make them suitable for various operations, including indexing, insertion, and deletion.
# While linked-lists and doubly-linked lists have their own advantages, Python's list type is optimized for a wide range of use cases, emphasizing performance and versatility.


