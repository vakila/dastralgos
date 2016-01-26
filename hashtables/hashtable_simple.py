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
        ht.append(None)


# Interface functions
def ht_set(key, value):
    """Adds value to the hashtable at the index for key.
    Returns True if the operation is successful.
    Returns False if there is already something at that index.
    """
    index = my_hash(key) % sz
    if ht[index] != None:
        return False
    else:
        ht[index] = value
        return True


def ht_get(key):
    """Returns the value for the given key.
    Return False if the key hasn't been used."""
    index = my_hash(key) % sz
    if ht[index] == None:
        return False
    else:
        return ht[index]

def ht_update(key, value):
    """If the key has been used in the hashtable, changes its value to value,
    and returns True.
    If the key hasn't been used, returns False.
    """
    index = my_hash(key) % sz
    if ht[index] == None:
        return False
    else:
        ht[index] = value
        return True

def ht_delete(key):
    """Sets the value stored at the given key's address to None.
    Returns True if successful, False if no such key exists."""
    index = my_hash(key) % sz
    if ht[index] == None:
        return False
    else:
        ht[index] = None
        return True


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()

    ht_init(3)
    print(ht)
    # print(ht_set('foo', 'bar'))
    # print(ht_get('foo'))
    # print(ht_update('foo', 'baz'))
    # print(ht_get('foo'))
    # print(ht_delete('foo'))
    # print(ht)

    for [k,v] in (['foo', 'bar'], ['fjkls','fjdksl'], ['ureuiwor', '4jio0s'], ['jfieo', '839204']):
        print([k,v], ": ht_set(k, v))
