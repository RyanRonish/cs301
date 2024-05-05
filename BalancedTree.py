class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    '''insert(item) inserts the item into the AVL tree, and ensures that the tree remains balanced.
        insert(item) average and worst = O(log(n))
    '''
    def insert(self, key):
        self.root = self._insert(self.root, key)
    def _insert(self, node, key):
        if not node:
            return TreeNode(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node
    
    '''delete(item) deletes the item from the AVL tree if it exists inside
    the list. After deletion, the resulting AVL tree should maintain the
    balanced property. If the item exists in the list and is removed, return
    True. Otherwise, if the item does not exist return False.
    delete(item) - average and worst case time complexity - O(log n)
    '''

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self._get_min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)

        if not root:
            return root

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        balance = self._get_balance(root)

        if balance > 1 and self._get_balance(root.left) >= 0:
            return self._right_rotate(root)
        if balance < -1 and self._get_balance(root.right) <= 0:
            return self._left_rotate(root)
        if balance > 1 and self._get_balance(root.left) < 0:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)
        if balance < -1 and self._get_balance(root.right) > 0:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    '''search(item) looks for the item in the AVL tree. If it exists, return
        True, otherwise return False.
        search(item) -- average and worst case time complexity - O(log n)
        '''

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if not root:
            return False
        elif root.key == key:
            return True
        elif key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)

    '''sortedList() returns the list of items in ascending sorted order in
        a list.
        sortedList() - O(n) - worst and avverage time complexity 
        '''

    def sortedList(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    '''reverseSortedList() returns the list of items in descending
        sorted order in a list.
        reverseSortedList() - O(n) average and worst case time complexity
        '''

    def reverseSortedList(self):
        result = []
        self._reverse_order(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    def _reverse_order(self, node, result):
        if node:
            self._reverse_order(node.right, result)
            result.append(node.key)
            self._reverse_order(node.left, result)

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current 





class PriorityQueue:
    def __init__(self):
        self.heap = []

        '''insert(item, key) inserts the item with its associated key into
        the priority queue. After insertion, ensure that the internal binary heap
        satisfies the heap order property.
        insert(item, key) - O(log n) average and worst case tiime complexity.'''

    def insert(self, item, key):
        self.heap.append((key, item))
        self._sift_up(len(self.heap) - 1)

        '''pop() returns a tuple (key, item) that is the item associated
        with the largest key in the queue. After popping, the priority queue
        should ensure that the internal binary heap maintains the heap order
        property.
        pop() - O(log n) aaverage and worst acase time complexity'''

    def pop(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        key, item = self.heap.pop()
        if self.heap:
            self._sift_down(0)
        return key, item
    
    '''returnQueue() returns a list representation of the priority queue
        that is ordered by how the contents of the queue will be returned by
        successive pop() operations. Note that this method does not return a
        list that if modified, modifies the original queue.
        returnQueue - O(1) average and worst case time complexity'''

    def returnQueue(self):
        return [(key, item) for key, item in self.heap]

    def _sift_up(self, idx):
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[parent_idx][0] < self.heap[idx][0]:
                self._swap(parent_idx, idx)
                idx = parent_idx
            else:
                break

    def _sift_down(self, idx):
        n = len(self.heap)
        while idx < n:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            largest = idx
            if left_child_idx < n and self.heap[left_child_idx][0] > self.heap[largest][0]:
                largest = left_child_idx
            if right_child_idx < n and self.heap[right_child_idx][0] > self.heap[largest][0]:
                largest = right_child_idx
            if largest != idx:
                self._swap(idx, largest)
                idx = largest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
      



# AVL tree
avl_tree = AVLTree()

avl_tree.insert(10)
avl_tree.insert(20)
avl_tree.insert(5)
avl_tree.insert(15)
avl_tree.insert(30)

print(avl_tree.search(20))  # Output: True
print(avl_tree.search(25))  # Output: False

avl_tree.delete(20)


print(avl_tree.sortedList())  # Output: [5, 10, 15, 30]

print(avl_tree.reverseSortedList())  # Output: [30, 15, 10, 5]

priority_queue = PriorityQueue()

priority_queue.insert('item1', 5)
priority_queue.insert('item2', 10)
priority_queue.insert('item3', 3)
priority_queue.insert('item4', 7)

print(priority_queue.pop())  # Output: (10, 'item2')
print(priority_queue.pop())  # Output: (7, 'item4')


print(priority_queue.returnQueue())  # Output: [(5, 'item1'), (3, 'item3')]


'''True
False
[5, 10, 15, 30]
[30, 15, 10, 5]
(10, 'item2')
(7, 'item4')
[(5, 'item1'), (3, 'item3')]'''