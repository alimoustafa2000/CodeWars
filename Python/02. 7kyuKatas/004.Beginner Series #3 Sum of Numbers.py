# DESCRIPTION:
# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!

# Examples (a, b) --> output (explanation)
# (1, 0)  --> 1 (1 + 0 = 1)
# (1, 2)  --> 3 (1 + 2 = 3)
# (0, 1)  --> 1 (0 + 1 = 1)
# (1, 1)  --> 1 (1 since both are same)
# (-1, 0) --> -1 (-1 + 0 = -1)
# (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)

# ============
# Solution:
# ============

def get_sum(a,b):

    if a > b:

        my_range = range(b, a+1)

    else:

        my_range = range(a, b+1)

    x = []

    for num in my_range:

        x.append(num)

    return sum(x)


print(get_sum(0,1))
# 1

print(get_sum(0,-1))
# -1

print(get_sum(-1, 2))
# 2
