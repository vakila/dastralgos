# Binary tree traversal algorithms

# from binary_tree import BinaryTreeNode
# class BinaryTreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
#     def is_leaf(self):
#         return self.left == None and self.right == None
#
#     def __str__(self):
#         return self.val

def visit(node):
    print(node)


def in_order(root):
    if root == None:
        return
    in_order(root.left)
    visit(root)
    in_order(root.right)

def pre_order(root):
    if root == None:
        return
    visit(root)
    pre_order(root.left)
    pre_order(root.right)

def post_order(root):
    if root == None:
        return
    post_order(root.left)
    post_order(root.right)
    visit(root)

if __name__ == "__main__":

    from sample_trees import *



    for sample in [tree_A, tree_B, tree_C, tree_D, tree_E, tree_F]:
        for traverse in [in_order, pre_order, post_order]:
            print("\nTraversing", sample.__name__, traverse.__name__)
            traverse(sample())
