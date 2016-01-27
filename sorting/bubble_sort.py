### Bubble sort in Python 3

def bubble_sort(my_list):
    '''Returns the sorted list (ascending) using this algorithm:
    Compare the first two items in the list. Swap them if necessary.
    Compare the second and third items. Swap them if necessary.
    Continue comparing each pair of adjacent items until list is sorted.
    After each pass through the list, one less item needs to be checked,
    because highest items percolate to the end of the list.
    '''
    print("Sorting list: ", my_list, "({0} items)".format(len(my_list)))
    done_i = len(my_list)
    while done_i != 0:
        # print("sorted past index:", done_i)
        for a in range(0, done_i-1):
            b = a+1
            # print("[", a, "]", my_list[a], "vs.", "[", b, "]", my_list[b])
            if my_list[a] > my_list[b] :
                # print("Swapping")
                my_list[a], my_list[b] = my_list[b], my_list[a]
        done_i -= 1
        # print(my_list)
    return my_list

if __name__ == "__main__":
    print(bubble_sort([4,2,1,3,5]), "\n")
    print(bubble_sort([2343, -43, 0, 1232, -586]), "\n")
    print(bubble_sort([1,2,3]), "\n")
    print(bubble_sort([1]), "\n")
    print(bubble_sort([]), "\n")
