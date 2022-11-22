# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.


def invert(lst):

    x = []

    for num in lst:

        x.append(num * -1)

    return x


print(invert([1,2,3,4,5]))
# [-1, -2, -3, -4, -5]