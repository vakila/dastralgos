# Given a tree, write an algorithm to determine whether or not the tree is
# (height-)balanced, i.e. whether the difference in depth between any two leaves
# is less than or equal to 1.

class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left == None and self.right == None



def check_balanced_with_depth(root_node, depth=0):
    if root_node.is_leaf():
        return (True, depth)

    children = {'left': root_node.left, 'right': root_node.right}
    balanced = {'left': True, 'right': True}
    depths = {'left': 0, 'right': 0}

    for side in ["left", "right"]:
        if children[side] != None:
            balanced[side], depths[side] = check_balanced(children[side],
                                                          depth = depth + 1)
        # else (children[side] == None) that side is balanced with depth 0


    tree_depth = max(depths.values()) + 1
    if False in balanced.values():
        return (False, tree_depth)
    else: #both are balanced, check depths
        depth_diff = max(depths.values()) - min(depths.values())
        depth_diff = abs(depths['left'] - depths['right'])
        return (depth_diff <= 1, tree_depth)


def check_balanced(root_node):
    return check_balanced_with_depth(root_node)[0]


def check_balanced_alt(root_node):
    max_depth = 0


    # traverse the tree until hitting a leaf
    # compare its depth to max depth
    # if the difference is too big, return False
    # else, if the leaf's depth is greater than max, set as new max
    # if you finish traversing without returning False, return True

if __name__ == "__main__":

    a = BinaryTreeNode('a')
    b = BinaryTreeNode('b')
    c = BinaryTreeNode('c')
    d = BinaryTreeNode('d')
    e = BinaryTreeNode('e')


    # Balanced tree A
    a.left = b
    a.right = c

    # Balanced tree B
    a.left = b

    # Balanced tree C
    a.left = b
    b.left = c
    b.right = d
    a.right = e

    # Unbalanced tree D
    a.left = b
    a.right = c
    c.left = d
    c.right = e
    e.right = f

    # Balanced tree E
    a.left = b
    b.left = c
    a.right = d
    d.right = e

    # Unbalanced tree F
    a.left = b
    a.right = c
    c.right = d
    d.right = e

    print(check_balanced(a))
