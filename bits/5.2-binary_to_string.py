# Given a number between 0 and 1 (e.g. 0.74), print the representation in binary.
# The input number is a double (64 bits).
# If the number can't be represented accurately with 32 digits, print "ERROR"

0.7962

0.1 = 00001


0   1    0    1         0       0    1
1   .5   .25   .125      .0625


0.75 = 011


def binary_to_string(decimal):
    if decimal == 1 or decimal == 0:
        return str(decimal)
    string_parts = []
    remaining = decimal
    digit = 1 #the power of 2 represented by this digit
    while total < decimal:
        if len(string_parts) >= 30:
            return "ERROR"
        digit = digit/2.0
        if digit <= remaining:
            string_parts.append(1)
            remaining -= digit
        else:
            string_parts.append(0)

    return "0." + "".join(string_parts)
