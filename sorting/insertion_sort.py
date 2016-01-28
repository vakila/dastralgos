### Insertion sort in Python 3

def insertion_sort(my_list):
    '''Returns the sorted list (ascending) using this algorithm:
    #TODO

    >>> print(insertion_sort([4,2,1,3,5]))
    [1, 2, 3, 4, 5]
    >>> print(insertion_sort([2343, -43, 0, 1232, -586]))
    [-586, -43, 0, 1232, 2343]
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
                my_list.remove(item)
                my_list.insert(p, item)
                # print(my_list)
    return my_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
