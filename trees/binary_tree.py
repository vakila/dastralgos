class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left is None and self.right is None

    def __str__(self):
        return str(self.val)
