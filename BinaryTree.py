class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

#insert() combines with insertLogic -- checks to see fi the tree is empty and a root node is created
#or insert() puts item in the correct subtree and returns the updated node
    def insert(self, item):
        if not self.root:
            self.root = TreeNode(item)
        else:
            self.insertLogic(self.root, item)

    def insertLogic(self, node, item):
        if node is None:
            return TreeNode(item)
        if item < node.value:
            node.left = self.insertLogic(node.left, item)
        elif item > node.value:
            node.right = self.insertLogic(node.right, item)
        return node

#search checks if a root exists, if it does the searchLogic() is called to search for the item or returns false
    def search(self, item):
        return self.searchLogic(self.root, item) if self.root else False

    def searchLogic(self, node, item):
        if node is None:
            return False
        if item == node.value:
            return True
        elif item < node.value:
            return self.searchLogic(node.left, item)
        else:
            return self.searchLogic(node.right, item)

#returns the values in ascending order, returns empty if theres no values in the tree
    def sortedlist(self):
        return self.sortedlistLogic(self.root) if self.root else []

    def sortedlistLogic(self, node):
        if node is None:
            return []
        return self.sortedlistLogic(node.left) + [node.value] + self.sortedlistLogic(node.right)

#returns the values in descending order, no values it returns an empty list
    def reverseSortedList(self):
        return self.reverseLogic(self.root) if self.root else []

    def reverseLogic(self, node):
        if node is None:
            return []
        return self.reverseLogic(node.right) + [node.value] + self.reverseLogic(node.left)


bst = BinaryTree()
test_nums = [5, 8, 12, 65, 7, 77, 41, 50, 27]

for test_num in test_nums:
    bst.insert(test_num)

print("Sorted list:", bst.sortedlist())
print("Reverse sorted list:", bst.reverseSortedList())
print("Search for 27:", bst.search(27))
print("Search for 55:", bst.search(55))

'''
insert() - Best Case 0(1) - when the tree is empty and the node is put in the root directly
        - Average Case 0(log n) - when the tree is balanced, the node is inserted in the middle making it a log complexity
        - worst case 0(n) - if the tree becomes a linked list, the new node is inserted at the end of the list.

search() - Best Case 0(1) - best case if the item is found at the root node
        - Average Case 0(log n) - when the tree is balanced, the item is found in the middle
        - worst case 0(n) - when the tree becomes a linked list, and we have to traverse through all nodes to find the item

sortedlist() - Best Case 0(n) - when the tree is balanced, and it goes through each of the nodes in a sorted order
        - Average Case 0(n log n) - the nodes are traversed in a sorted manner with logarithmic time complexity per node
        - worst case 0(n^2) - when the tree becomes a linked list, and each recursive call traverses through all the nodes

reverseSortedList() - Best Case 0(n) - when the tree is balanced, and it goes through each of the nodes in a sorted order
        - Average Case 0(n log n) - the nodes are traversed in a sorted manner with logarithmic time complexity per node
        - worst case 0(n^2) - when the tree becomes a linked list, and each recursive call traverses through all the nodes
'''
