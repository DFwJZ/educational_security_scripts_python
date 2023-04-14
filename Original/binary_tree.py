# Define the TreeNode class, which represents a single node in a binary search tree.
class TreeNode:
    def __init__(self, value):
        self.value = value  # The value stored in the node
        self.left = None    # The left child of the node
        self.right = None   # The right child of the node

# Define the BinarySearchTree class, which represents a binary search tree data structure.
class BinarySearchTree:
    def __init__(self):
        self.root = None  # The root node of the tree

    # Public method to insert a value into the tree.
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    # Helper method to insert a value into the tree recursively.
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)