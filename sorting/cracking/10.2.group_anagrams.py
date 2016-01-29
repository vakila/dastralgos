# 10.2 Group Anagrams
# Write a method to sort an array of strings so that all the anagrams are next to each other.
from collections import default_dict

def group_anagrams(string_list):
    '''Groups anagrams in a list of strings by sorting each string
    to obtain its list of characters and building a dictionary to group
    of the original (unsorted) anagrams from string_list by
    alphabetized key. The dictionary's values are then concatenated
    together to form the final list of anagram groups that is returned.
    Strings that are anagrams of each other will be next to each other,
    but the groups of anagrams will not be sorted.
    '''
    groups = default_dict(list)

    for string in string_list:
        alphabetical = sort(string)
        groups[alphabetical].append(string)

    result = []
    for group, strings in groups.items():
        result += strings
    return result


if __name__ == "__main__":
    assert merge_sort("dcefab") == "abcdef"
