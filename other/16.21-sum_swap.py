# Given two lists of integers, ....


def sum_swap(a, b):
    sum_a = sum(a)
    sum_b = sum(b)
    pair_distance = (sum_a - sum_b)/2

    complements = dict()

    for x in a:
        to_swap = x + pair_distance
        complements[to_swap] = x

    for y in b:
        if y in complements:
            return (complements[y], y)

    return None

def sum_swap_no_dict(a, b):
    '''Requires a and b to be sorted'''
    sum_a = sum(a)
    sum_b = sum(b)
    pair_distance = (sum_a - sum_b)/2

    i_a = 0
    i_b = 0

    while i_a < len(a) and i_b < len(b):
        x = a[i_a]
        y = b[i_b]

        if x - y == pair_distance:
            return (x, y)
        elif x - y < pair_distance:
            i_a += 1
        else:
            i_b += 1

    return None



result = sum_swap([4,1,2,1,1,2], [3,6,3,3])
