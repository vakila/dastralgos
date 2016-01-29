### Quick sort in Python 3

# Performance:
# Best/average case: O(n log n)
# Worst case: O(n^2)

def quick_sort(my_list):
    '''Returns the sorted list (ascending) using this algorithm:
    Choose a "pivot" element (somehow) from the array.

    "Partition" the array such that all elements lower than the pivot
    are to the left of the pivot, and all high elements are to the right.

    Do this by working inwards from the left end of the array until you find
    an element greater than the pivot, then working inwards from the right end
    until you find an element less than the pivot,
    and swapping them if appropriate. (That is the CtCI way; are there others?)

    Recursively sort the slices of the array to the left and right of the pivot.

    '''
    # TODO
    return my_list


if __name__ == "__main__":
    assert(quick_sort([4,2,1,3,5])) == [1, 2, 3, 4, 5]
    assert(quick_sort([2343, -43, 0, 1232, -586])) == [-586, -43, 0, 1232, 2343]
    assert(quick_sort([1,2,3])) == [1, 2, 3]
    assert(quick_sort([1])) == [1]
    assert(quick_sort([])) == []
