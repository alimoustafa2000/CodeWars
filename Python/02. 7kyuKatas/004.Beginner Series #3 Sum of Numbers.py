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
