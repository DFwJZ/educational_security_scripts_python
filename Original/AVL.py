# Define the AVLNode class, which represents a single node in an AVL tree.
class AVLNode:
    def __init__(self, value):
        self.value = value  # The value stored in the node
        self.left = None    # The left child of the node
        self.right = None   # The right child of the node
        self.height = 1     # The height of the node

# Define the AVLTree class, which represents an AVL tree data structure.
class AVLTree:
    def __init__(self):
        self.root = None  # The root node of the tree

    # Public method to insert a value into the tree.
    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    # Helper method to insert a value into the tree recursively.
    def _insert_recursive(self, node, value):
        # If the current node is None, create a new node with the value.
        if node is None:
            return AVLNode(value)

        # If the value is less than the node's value, insert it into the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            # Otherwise, insert it into the right subtree.
            node.right = self._insert_recursive(node.right, value)

        # Update the height of the current node.
        node.height = 1 + max(self._height(node.left), self._height(node.right))

        # Calculate the balance factor of the current node.
        balance = self._balance(node)

        # If the balance factor is greater than 1, perform rotations to balance the tree.
        if balance > 1:
            if value < node.left.value:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)

        # If the balance factor is less than -1, perform rotations to balance the tree.
        if balance < -1:
            if value > node.right.value:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

        # If the balance factor is between -1 and 1, return the current node.
        return node

    # Helper method to calculate the height of a given node.
    def _height(self, node):
        if node is None:
            return 0
        return node.height

    # Helper method to calculate the balance factor of a given node.
    def _balance(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    # Helper method to perform a left rotation around a given node.
    def _left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))

        return new_root

    # Helper method to perform a right rotation around a given node.
    def _right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        new_root.height = 1 + max(self._height(new_root.left), self._height(new_root.right))

        return new_root
