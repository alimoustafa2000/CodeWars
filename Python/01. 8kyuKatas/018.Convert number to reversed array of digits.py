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