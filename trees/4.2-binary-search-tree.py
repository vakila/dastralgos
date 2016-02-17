# Given a sorted array of numbers, write an algorithm to construct
# a binary search tree (all nodes to the left of a given node are lower,
# all nodes to the right are higher).

from binary_tree import BinaryTreeNode

def to_search_tree(sorted_list):
    print("List:", sorted_list)
    if len(sorted_list) == 0:
        print("Empty list, returning None")
        return None
    elif len(sorted_list) == 1:
        print("Single entry, creating new node")
        return BinaryTreeNode(sorted_list[0])
    else:
        print("2 or more entries. Splitting and recursing.")
        mid = len(sorted_list)//2
        root = BinaryTreeNode(sorted_list[mid])
        print("Root (midpoint of split):", root)
        root.left = to_search_tree(sorted_list[:mid])
        root.right = to_search_tree(sorted_list[mid+1:])
        return root


if __name__ == "__main__":

    from traverse_binary_tree import in_order

    listy = [1, 3, 5, 7]

    root = to_search_tree(listy)

    print(listy)

    in_order(root)
