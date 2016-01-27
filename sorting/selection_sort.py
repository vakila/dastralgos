### Selection sort in Python 3

def selection_sort(my_list):
    '''Returns the list with items sorted from lowest to highest using this algorithm:
    - Go through each item in the array to find the smallest.
    - Swap the smallest item with the item at the start of the array.
      The first item in the array is now done being sorted.
    - Go through the remainder of the array and find the next smallest item.
    - Swap that item with the second item in the array.
      The first and second items are now done being sorted.
    - Continue this way until the whole array has been sorted.

    >>> print(selection_sort([4,2,1,6,3]))
    [1, 2, 3, 4, 6]
    >>> print(selection_sort([58940, -343, 1, 0, -34]))
    [-343, -34, 0, 1, 58940]
    >>> print(selection_sort([]))
    []
    >>> print(selection_sort([0]))
    [0]
    >>> print(selection_sort([1,2,3]))
    [1, 2, 3]
    '''
    #print(my_list)
    for slot in range(len(my_list)-1):
        #print("at slot:", slot)
        min_i = slot
        for i in range(slot, len(my_list)):
            if my_list[i] < my_list[min_i]:
                min_i = i
                #print("smallest:", my_list[min_i], "[{0}]".format(min_i))
        my_list[slot], my_list[min_i] = my_list[min_i], my_list[slot]
        #print(my_list)
    return my_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
