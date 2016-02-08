# Explaining Big O 

ints = [1,2,4,5,6,7]

def two_loops(): # O(n+n) = O(2n) = O(n)
    for i in ints: #O(n)
        print(i)
    for j in ints: #O(n)
        print(j)




def nested_loops(): # O(n*n) = O(n^2)
    for i in ints: #O(n)
        for j in ints: #O(n)
            print(j-i)



def contains_a(string):
    for char in string:
        if char == 'a':
            return true
    return false


contains_a("anjananananananananananan") # best case

contains_a("khalid") # average case

contains_a("nicknicknicknicknick") # worst case
