# DESCRIPTION:
# You are given two interior angles (in degrees) of a triangle.
# Write a function to return the 3rd.

# Note: only positive integers will be tested.

# ============
# Solution:
# ============

def other_angle(a, b):

    c = 180 - int((a + b))

    return c

print(other_angle(30, 60))
# 90
