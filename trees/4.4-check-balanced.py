class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left == None and self.right == None



def check_balanced_old(root_node, depth=0):
    left_balanced, left_depth = check_balanced(root_node.left, depth = depth+1)
    right_balanced, right_depth = check_balanced(root_node.right, depth = depth+1)

    if not (left_balanced and right_balanced):
        return (False, max(left_depth, right_depth)+1))
    else: #both are balanced, check depths
        return abs(left_depth - right_depth) <= 1


def check_balanced(root_node):
    max_depth = 0

    # traverse the tree until hitting a leaf
    # compare its depth to max depth
    # if the difference is too big, return False
    # else, if the leaf's depth is greater than max, set as new max
    # if you finish traversing without returning False, return True
