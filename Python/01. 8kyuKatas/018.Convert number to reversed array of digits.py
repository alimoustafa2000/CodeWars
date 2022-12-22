# DESCRIPTION:
# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]

# ============
# Solution:
# ============

def digitize(n):

    z = []

    a = str(n)

    x = list(a)

    x.reverse()

    for num in x:

        y = int(num)

        z.append(y)

    return z

print(digitize(35231))
# [1, 3, 2, 5, 3]