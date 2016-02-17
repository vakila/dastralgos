# Count number of inverted pairs in a list of numbers.
# Given indices i and j, a pair is inverted if
# i < j and list[i] > list[j].

# The maximum possible number of inversions in a list of length n
# (if list is sorted from highest to lowest)
# is n choose 2, i.e. n(n-1)/2


# Naive brute force approach
# O(n^2)

def count_invs(listy):
    inversions = 0
    for i in range(len(listy)):
        for j in range(i, len(listy)):
            if listy[i] > listy[j]:
                inversions += 1
    return inversions


# Recursive approach
# Modeled on merge sort
# O(n log n)

def sort_and_count_invs(listy):
    n = len(listy)
    print("Sorting and counting:", listy, "({0} items)".format(n))

    if n < 2:
        print("Less than two items.")
        merged = listy
        invs = 0
    elif n == 2:
        if listy[0] > listy[1]:
            # Put the two in the correct order
            merged = listy[::-1]
            invs = 1
        else:
            merged = listy
            invs = 0
    else:
        middle = len(listy)//2
        left, l_invs = sort_and_count_invs(listy[:middle])
        right, r_invs = sort_and_count_invs(listy[middle:])
        merged, s_invs = merge_and_count_split_invs(left, right)
        invs = l_invs + r_invs + s_invs
    print("merged:", merged, "invs:", invs)
    return (merged, invs)


def merge_and_count_split_invs(left, right):
    # assume left and right are independently sorted
    print("Merging and counting:", left, right)
    if left[0] > right[-1]:
        print("Two independent halves, wrong order")
        merged = right + left
        invs = len(left) * len(right)
    elif right[0] > left[-1]:
        print("Two independent halves, correct order")
        merged = left + right
        invs = 0
    else:
        print("Interleaving halves, merging...")
        l_i = r_i = 0
        invs = 0
        merged = []
        # while l_i < len(left) and r_i < len(right):
        while len(merged) < len(left) + len(right):
            left_item = left[l_i]
            right_item = right[r_i]
            print("left:  [{0}] {1}".format(l_i, left_item))
            print("right: [{0}] {1}".format(r_i, right_item))

            if left_item > right_item:
                print("Pair inverted. Adding", right_item, "to merged")
                invs += len(left) - l_i
                merged.append(right_item)
                r_i += 1
            else:
                print("Pair OK. Adding", left_item, "to merged")
                merged.append(left_item)
                l_i += 1
            print("Merged:", merged)
            if l_i == len(left):
                # Reached end of left; add remainder of right
                merged += right[r_i:]
            elif r_i == len(right):
                # Reached end of right; add remainder of left
                merged += left[l_i:]
    print("Final merged:", merged)
    print("Inversions:", invs)
    return (merged, invs)


# Run simple tests
if __name__ == "__main__":
    assert(sort_and_count_invs([6, 5, 4, 3, 2, 1])[1] == 15)
    assert(sort_and_count_invs([1, 2, 3])[1] == 0)
    assert(sort_and_count_invs([1, 3, 2, 4, 5, 6])[1] == 1)
    assert(sort_and_count_invs([1, 2, 3, 4, 6, 5])[1] == 1)
    assert(sort_and_count_invs([1, 3, 2, 4, 6, 5])[1] == 2)
    assert(sort_and_count_invs([1, 4, 6, 2, 3, 5])[1] == 5)
    assert(sort_and_count_invs([5, 4, 3, 2, 1])[1] == 10)
    assert(sort_and_count_invs([])[1] == 0)
    assert(sort_and_count_invs([8, 7, 6, 5, 4, 3, 2, 1, 0])[1] == 36)

    # assert(merge_and_count_split_invs([1, 2, 3], [4, 5, 6]) == ([1, 2, 3, 4, 5, 6], 0))
    # assert(merge_and_count_split_invs([2, 4, 6], [1, 3, 5]) == ([1, 2, 3, 4, 5, 6], 6))
    # assert(merge_and_count_split_invs([1, 3, 5], [2, 4, 6]) == ([1, 2, 3, 4, 5, 6], 3))
    # assert(merge_and_count_split_invs([4, 5, 6], [1, 2, 3]) == ([1, 2, 3, 4, 5, 6], 9))
    # assert(merge_and_count_split_invs([4, 5], [1, 2, 3]) == ([1, 2, 3, 4, 5], 6))
    # assert(merge_and_count_split_invs([4, 5, 6], [1, 2]) == ([1, 2, 4, 5, 6], 6))
