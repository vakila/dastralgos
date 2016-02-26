# In CtCI you're asked to imagine building a diving board of variable length
# with two types of planks, of two different lengths (l1 and l2).
# Using k planks, what are all your options for the length of the board?
# (here reframed as building a bridge instead)

def bridge_length(k, l1, l2):
    lengths = []
    for numl1 in range(0, k+1):
        numl2 = k - numl1
        length = numl1 * l1 + numl2 * l2
        lengths.append(length)
    return lengths

print(bridge_length(10, 1, 2))


print(bridge_length(5, 2, 3))
