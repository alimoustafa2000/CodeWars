# DESCRIPTION:
# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
# Return your answer as a number.

# ============
# Solution:
# ============

def sum_mix(arr):

    x = []

    for num in arr:

        x.append(int(num))

    return sum(x)


print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]))
# 42

