### Insertion sort in Python 3

# Performance:
# Best case (input list is sorted): O(n)
# Average case (input is shuffled): O(n^2)
# Worst case (input is in reverse order): O(n^2)

def insertion_sort(my_list):
    '''Returns the sorted list (ascending) using this algorithm:
    Look at the second item in the list.
    Compare it to its neighbor on the left;
        if the item is smaller than the neighbor, swap them.
    Continue comparing with leftmost neighbors until either:
        - the item is larger than the left neighbor
        - you've reached the beginning of the list.
    Continue with the next item in the list, until you reach the end.
    

    >>> print(insertion_sort([4,2,1,3,5]))
    [1, 2, 3, 4, 5]
    >>> print(insertion_sort([2343, -43, 0, 1232, -586]))
    [-586, -43, 0, 1232, 2343]
    >>> print(insertion_sort([2,3,2,1]))
    [1, 2, 2, 3]
    >>> print(insertion_sort([1,2,3]))
    [1, 2, 3]
    >>> print(insertion_sort([1]))
    [1]
    >>> print(insertion_sort([]))
    []
    '''
    # print("Sorting:", my_list)
    for i in range(1, len(my_list)):
        # print("i:", i)
        item = my_list[i]
        for p in range(i-1,-1,-1):
            previous = my_list[p]
            # print("item:", item, "previous:", previous, "[{0}]".format(p))
            if item >= previous:
                # print("item is bigger, exiting inner loop")
                break
            else:
                # print("item is smaller, moving left")
                my_list[p], my_list[p+1] = item, previous
                # print(my_list)
    return my_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
