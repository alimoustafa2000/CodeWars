# DESCRIPTION:
# Summation
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

# For example (Input -> Output):
# 2 -> 3 (1 + 2)
# 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)

# ============
# Solution:
# ============

def summation(num):

    return sum(range(1, num+1))


print(summation(100))
# 5050  
print(summation(22))
# 253