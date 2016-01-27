# 10.1 Sorted Merge
# You are given two sorted arrays, A and B, where A has a large enough buffer
# to hold B. Write a method to merge B into A in sorted order.

def sorted_merge(a, b):
    '''Returns a list with the sorted lists a and b merged in sorted order.
    >>> sorted_merge([1, 3, 5], [2, 4])
    [1, 2, 3, 4, 5]
    >>> sorted_merge([2, 4], [1, 3, 5])
    [1, 2, 3, 4, 5]
    >>> sorted_merge([1, 3, 5], [])
    [1, 3, 5]
    >>> sorted_merge([], [1, 3, 5])
    [1, 3, 5]
    >>> sorted_merge([5, 6], [1, 2, 3, 4])
    [1, 2, 3, 4, 5, 6]
    '''
    a_i = 0
    b_i = 0
    c = []
    while a_i < len(a) and b_i < len(b):
        # print("c:", c)
        # print("a_i:", a_i, "b_i:", b_i)
        this_a = a[a_i]
        this_b = b[b_i]
        if this_a >= this_b:
            c.append(this_b)
            b_i += 1
        if this_a <= this_b:
            c.append(this_a)
            a_i += 1
    if a_i == len(a):
        # print("adding rest of b")
        c += b[b_i:]
    if b_i == len(b):
        # print("adding rest of a")
        c += a[a_i:]
    return c

def sorted_merge_in_place(a, b):
    '''Same as above without using new list.
    >>> sorted_merge_in_place([1, 3, 5], [2, 4])
    [1, 2, 3, 4, 5]
    >>> sorted_merge_in_place([2, 4], [1, 3, 5])
    [1, 2, 3, 4, 5]
    >>> sorted_merge_in_place([1, 3, 5], [])
    [1, 3, 5]
    >>> sorted_merge_in_place([], [1, 3, 5])
    [1, 3, 5]
    >>> sorted_merge_in_place([5, 6], [1, 2, 3, 4])
    [1, 2, 3, 4, 5, 6]
    '''
    a_i = 0
    b_i = 0
    while b_i < len(b):
        # print("a:", a)
        # print("a_i:", a_i, "b_i:", b_i)
        this_b = b[b_i]
        if a_i == len(a) or a[a_i] >= this_b:
            a.insert(a_i, this_b)
            b_i += 1
        a_i += 1
    return a


if __name__ == "__main__":
    # print(sorted_merge_in_place([2, 4], [1, 3, 5]))
    import doctest
    doctest.testmod()
