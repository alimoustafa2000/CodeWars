# DESCRIPTION:
# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.
# You receive an array with your peers' test scores. Now calculate the average and compare your score!
# Return True if you're better, else False!

# Note:
# Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!

# ============
# Solution:
# ============

def better_than_average(class_points, your_points):

    a = sum(class_points) + your_points

    b = len(class_points) + 1

    x = a / b

    if x < your_points:

        return True

    else:

        return False


print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))
# True

print(better_than_average([29, 55, 74, 60, 11, 90, 67, 28], 21))
# False