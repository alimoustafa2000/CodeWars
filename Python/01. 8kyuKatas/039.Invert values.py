# DESCRIPTION:
# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []

# You can assume that all values are integers. Do not mutate the input array/list.

# ============
# Solution:
# ============

def invert(lst):

    x = []

    for num in lst:

        x.append(num * -1)

    return x


print(invert([1,2,3,4,5]))
# [-1, -2, -3, -4, -5]