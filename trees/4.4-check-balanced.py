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

    def __str__(self):
        return self.val


def balanced_with_depth(root_node, depth=0):
    print("TREE", "root:", root_node, "depth:", depth)

    children = {'left': root_node.left, 'right': root_node.right}
    depths = {'left': depth, 'right': depth}

    for side in ["left", "right"]:
        print("-"*(depth+1), side.upper(), end=" ")
        if children[side] == None:
            print("EMPTY CHILD")
            depths[side] = depth
        else:
            balanced, depths[side] = balanced_with_depth(children[side],
                                                         depth = depth + 1)
            if balanced == False:
                print(" "*depth, "UNBALANCED subtree", side)
                return (False, depths[side])
        # else (children[side] == None) that side is balanced with depth 'depth'

    tree_depth = max(depths.values())

    # any major difference/advantage between the 2 lines below?
    depth_diff = max(depths.values()) - min(depths.values())
    # depth_diff = abs(depths['left'] - depths['right'])

    print("-"*depth, "TREE", root_node, "BALANCED?", depth_diff <= 1, "(depths:", depths, ")")
    return (depth_diff <= 1, tree_depth)

def check_balanced(root_node):
    answer, depth = balanced_with_depth(root_node)
    print("\nROOT:", root_node.val, "DEPTH:", depth, "BALANCED?", answer)
    return answer

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
    f = BinaryTreeNode('f')

    '''Uncomment one of the tree definitions below to test that tree'''

    # print("Testing Tree A: Balanced")
    # a.left = b
    # a.right = c

    # print("Testing Tree B: Balanced")
    # a.left = b

    # print("Testing Tree C: Balanced")
    # a.left = b
    # b.left = c
    # b.right = d
    # a.right = e

    # print("Testing Tree D: Unbalanced")
    # a.left = b
    # a.right = c
    # c.left = d
    # c.right = e
    # e.right = f

    # print("Testing Tree E: Balanced")
    # a.left = b
    # b.left = c
    # a.right = d
    # d.right = e

    print("Testing Tree F: Unbalanced")
    a.left = b
    a.right = c
    c.right = d
    d.right = e

    print(check_balanced(a))
