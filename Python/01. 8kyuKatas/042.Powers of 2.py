# Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).

# Examples
# n = 0  ==> [1]        # [2^0]
# n = 1  ==> [1, 2]     # [2^0, 2^1]
# n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]

# ============
# Solution:
# ============

def powers_of_two(n):

    z = []

    for x in range(0,n+1):

        z.append(2**x)

    return z


print(powers_of_two(4))
# [1, 2, 4, 8, 16]