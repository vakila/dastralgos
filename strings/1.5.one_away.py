# 1.5 One Away
# There are three types of edits that can be performed on strings:
# insert, delete, or replace a character. Given two strings, write a function
# to check if they are one edit (or zero edits) away.


def one_away(a, b):
    print("\na: '{0}' b: '{1}'".format(a, b))
    ## Special cases can be evaluated immediately
    if a == b:
        # no edits
        print("Identical")
        return True
    if abs(len(a) - len(b)) > 1:
        # 2 or more insertions/deletions
        print("2 or more insertions/deletions")
        return False
    else:
        ## Have to count the edits manually
        # pointers to simultaneously iterate over both strings:
        a_i = 0
        b_i = 0
        # edit counter
        edits = 0
        while a_i < len(a):
            print("a_i: {0}, b_i: {1}".format(a_i, b_i))
            old = a[a_i]
            try:
                new = b[b_i]
            except IndexError:
                # last character of a was deleted
                print("character deleted at end")
                edits += 1
                break
            else:
                if old != new:
                    edits += 1
                    try:
                        deleted = new == a[a_i+1]
                    except IndexError:
                        deleted = False
                    try:
                        inserted = old == b[b_i+1]
                    except IndexError:
                        inserted = False
                    if deleted:
                        # a[a_i] was deleted, advance a_i
                        print("character deleted")
                        a_i += 1
                    elif inserted:
                        # character was inserted at a_i, advance b_i
                        print("character inserted")
                        b_i += 1
                    else:
                        print("character replaced")
                        a_i += 1
                        b_i += 1
                else:
                    # no edit, advance both pointers
                    print("no edit")
                    a_i += 1
                    b_i += 1
        if b_i == len(b)-1:
            # character was inserted at end of a
            print("character inserted at end")
            edits += 1
        print(edits, "edits")
        return edits <= 1



if __name__ == "__main__":

    # assert(one_away("pale", "ple") == True)
    # assert(one_away("pales", "pale") == True)
    # assert(one_away("pale", "pales") == True)
    # assert(one_away("pale", "bale") == True)
    # assert(one_away("pale", "pale") == True)
    # assert(one_away("pale", "bake") == False)
    # assert(one_away("pale", "pl") == False)
    # assert(one_away("pale", "spales") == False)
    # assert(one_away("pale", "pable") == True)
    # assert(one_away("pale", "pabe") == True)
    # assert(one_away("pale", "plle") == True)
    assert(one_away("pale", "pastl") == False)
