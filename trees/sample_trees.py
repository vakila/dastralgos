from binary_tree import BinaryTreeNode

def node_a():
    return BinaryTreeNode('a')
def node_b():
    return BinaryTreeNode('b')
def node_c():
    return BinaryTreeNode('c')
def node_d():
    return BinaryTreeNode('d')
def node_e():
    return BinaryTreeNode('e')
def node_f():
    return BinaryTreeNode('f')


# Tree A: Balanced
def tree_A():
    a = node_a()
    a.left = node_b()
    a.right = node_c()
    return a

# Tree B: Balanced
def tree_B():
    a = node_a()
    a.left = node_b()
    return a

# Tree C: Balanced
def tree_C():
    a = node_a()
    a.left = b = node_b()
    b.left = node_c()
    b.right = node_d()
    a.right = node_e()
    return a

# Tree D: Unbalanced
def tree_D():
    a = node_a()
    a.left = node_b()
    a.right = c = node_c()
    c.left = node_d()
    c.right = e = node_e()
    e.right = node_f()
    return a

# Tree E: Balanced
def tree_E():
    a = node_a()
    a.left = b = node_b()
    b.left = node_c()
    a.right = d = node_d()
    d.right = node_e()
    return a

# Tree F: Unbalanced
def tree_F():
    a = node_a()
    a.left = node_b()
    a.right = c = node_c()
    c.right = d = node_d()
    d.right = node_e()
    return a
