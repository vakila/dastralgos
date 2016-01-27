### Basic search algorithms in Python 3

def linear_search(my_list, value):
    '''Takes a list (needn't be sorted) and a value to search for.
    Returns the index of (the first occurrence of) value in my_list.
    If my_list does not contain value, returns None.
    Searches for value simply by examining each item in the list.

    >>> print(linear_search([1,3,2,5,4], 2))
    2
    >>> print(linear_search([1,3,4,2,2], 2))
    3
    >>> print(linear_search([1,3,2,4,2], 5))
    None
    '''
    for i in range(len(my_list)):
        if my_list[i] == value:
            return i
    return None

def binary_search(sorted_list, value):
    '''Takes a sorted list (low to high) and a value to search for.
    Returns the index of (the first occurrence of) value in my_list.
    If my_list does not contain value, returns None.
    Searches for value using a simple binary search.

    >>> print(binary_search([1,2,3,4,5], 1))
    0
    >>> print(binary_search([1,2,3,4,5,6], 5))
    4
    >>> print(binary_search([1,2,3,4,5], 2))
    1
    >>> print(binary_search([1,2,3,4,5,6], 7))
    None
    >>> print(binary_search([1,2,3,4,5], 0))
    None
    '''
    # print("Searching for", value, "in", sorted_list)
    low = 0
    high = len(sorted_list)-1
    while low <= high:
        # print("searching from [{0}] to [{1}]".format(low, high))
        midpoint = int((high+low)/2)
        # print("midpoint [{0}]:".format(midpoint), sorted_list[midpoint])
        if value < sorted_list[midpoint]:
            # print("value is lower")
            high = midpoint-1
        elif value > sorted_list[midpoint]:
            # print("value is higher")
            low = midpoint+1
        else:
            # print("found value")
            return midpoint
    return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()
