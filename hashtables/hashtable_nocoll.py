# Hash table implementation
# Jobs prep Friday - 2015-10-09

# hashing function
def my_hash(key_string):
    """Return a unique hash for the string some_key

    Uses ord(character) to return the ASCII value for a given character

    Examples:

    >>> my_hash("abc")
    294
    >>> my_hash("hello")
    532
    >>> my_hash("hellp")
    533
    >>> my_hash("helmp")
    534

    """
    my_hash = 0
    for char in key_string:
        my_hash += ord(char) #gets ASCII value of char and adds

    return my_hash

# Initialization function
def ht_init(size):
    """Creates an array of the given size representing the hash table.
    The array contains only None.
    The array is declared as a global variable ht.
    """
    global ht
    ht = []
    global sz
    sz = size

    for i in range(sz):
        ht.append([])


# Interface functions
def ht_set(key, value):
    """Adds tuple (key, value) to the list at the index for key
    in the hashtable.
    Returns the number of items in the list at that index.
    """
    print("setting ", key, " to ", value)
    index = my_hash(key) % sz
    ht[index].append((key,value))
    return len(ht[index])


def ht_get(key):
    """Returns the value for the given key.
    Return False if the key hasn't been used."""
    print("getting ", key)
    index = my_hash(key) % sz
    found_it = False
    for (k, v) in ht[index]:
        if k == key:
            found_it = v
    return found_it # returns False if not found, or the value

def ht_update(key, value):
    """If the key has been used in the hashtable, changes its value to value,
    and returns True.
    If the key hasn't been used, returns False.
    """
    print("updating ", key, " to ", value)
    index = my_hash(key) % sz
    found_it = False
    for (k, v) in ht[index]:
        if k == key:
            found_it = True
            ht[index].remove((k, v))
            ht[index].append((key, value))
    # possibly faster approach:
    # for (i, (k, v)) in enumerate(ht[index]):
    #     if k == key:
    #         ht[index][i] = (key, value)
    return found_it

def ht_delete(key):
    """Sets the value stored at the given key's address to None.
    Returns True if successful, False if no such key exists."""
    print("deleting ", key)
    index = my_hash(key) % sz
    found_it = False
    for (k, v) in ht[index]:
        if k == key:
            found_it = True
            ht[index].remove((k, v))
    return found_it

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()

    ht_init(3)
    # print(ht)
    # print(ht_set('foo', 'bar'))
    # print(ht)
    #
    # print(ht_get('foo'))
    # print(ht)
    #
    # print(ht_update('foo', 'baz'))
    # print(ht)
    #
    # print(ht_get('foo'))
    # print(ht)
    #
    # print(ht_delete('foo'))
    # print(ht)

    for [k,v] in (['foo', 'bar'], ['fjkls','fjdksl'], ['ureuiwor', '4jio0s'], ['jfieo', '839204']):
        print([k,v], ": ", ht_set(k, v))
    print(ht)
