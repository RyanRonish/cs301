class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

class DirectoryTree:
    def __init__(self, root='/'):
        self.root = TreeNode(root)

    # Big O - O(n^2) because you might go through all children nodes of current node
    def insert_file(self, path):
        directories = path.split('/')
        current_node = self.root

        for directory in directories[1:]:
            found = False
            for child in current_node.children:
                if child.data == directory:
                    current_node = child
                    found = True
                    break
            if not found:
                new_node = TreeNode(directory)
                current_node.children.append(new_node)
                current_node = new_node

    # Big O - O(n^2) because you might go through all childen of current node
    def delete_file(self, path):
        directories = path.split('/')
        current_node = self.root

        for directory in directories[1:]:
            found = False
            for child in current_node.children:
                if child.data == directory:
                    current_node = child
                    found = True
                    break
            if not found:
                raise IndexError('File Not Found')

        if current_node.data != directories[-1]:
            raise IndexError('File Not Found')

        parent_node = self.find_parent(path)
        parent_node.children = [child for child in parent_node.children if child.data != directories[-1]]

    # Big O - O(n^2) because move_file is the sum of the insert_file and delete_file
    def move_file(self, source_path, destination_path):
        try:
            self.insert_file(destination_path)
            self.delete_file(source_path)
        except IndexError as e:
            raise IndexError(str(e))

    def find_parent(self, path):
        directories = path.split('/')
        current_node = self.root

        for directory in directories[1:-1]:
            found = False
            for child in current_node.children:
                if child.data == directory:
                    current_node = child
                    found = True
                    break
            if not found:
                raise IndexError('File Not Found')

        return current_node

    def recursive(self, node, indent=0):
        if node:
            if node.data is not None:
                print(' ' * indent + node.data)
            for child in node.children:
                self.recursive(child, indent + 10)

    def print_tree(self):
        self.recursive(self.root)


# Example usage:
tree = DirectoryTree()
file_paths = [
    '/usr',
    '/var/log/log1.log',
    '/var/log/log2.log',
    '/dev/null',
    '/dev/code/include',
    '/dev/code/include/lib',
    '/usr/patch',
    '/usr/patch/log/log2.log',
    '/usr/patch/log/log3.log',
    '/mnt/c/users/local/program_data/VSCode/data.py'
]

for path in file_paths:
    tree.insert_file(path)

tree.print_tree()