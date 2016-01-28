### Merge sort in Python 3

# Performance:
# Best/average/worst case: O(n log n)

def merge_sort(my_list):
    '''Returns the sorted list (ascending) using this algorithm:
    If the list only has one element, return.
    Otherwise, split the list into two halves.
    Recursively sort each half.
    Merge the two halves (now sorted) together, preserving the sort order.

    '''
    print("Sorting:", my_list)
    if len(my_list) <= 1:
        return my_list
    else:
        midpoint = int(len(my_list)/2)
        left = merge_sort(my_list[:midpoint])
        right = merge_sort(my_list[midpoint:])
        merged = merge_lists(left, right)
        print(merged)
        return merged

def merge_lists(a, b):
    '''Merges two sorted lists, preserving the sort order.
    '''
    print("Merging", a, "and", b)
    longer, shorter = (a,b) if len(a) > len(b) else (b,a)
    i = 0
    while len(shorter) > 0:
        if i == len(longer):
            return longer + shorter
        elif longer[i] >= shorter[0]:
            longer.insert(i, shorter.pop(0))
        i += 1
    return longer

if __name__ == "__main__":
    # assert merge_lists([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]
    # assert merge_lists([2, 4], [1, 3, 5]) == [1, 2, 3, 4, 5]
    # assert merge_lists([1, 3, 5], []) == [1, 3, 5]
    # assert merge_lists([], [1, 3, 5]) == [1, 3, 5]
    # assert merge_lists([5, 6], [1, 2, 3, 4]) == [1, 2, 3, 4, 5, 6]

    assert merge_sort([4,2,1,3,5]) ==  [1, 2, 3, 4, 5]
    assert merge_sort([2343, -43, 0, 1232, -586]) ==  [-586, -43, 0, 1232, 2343]
    assert merge_sort([2,3,2,1]) ==  [1, 2, 2, 3]
    assert merge_sort([1,2,3]) ==  [1, 2, 3]
    assert merge_sort([1]) ==  [1]
    assert merge_sort([]) ==  []
