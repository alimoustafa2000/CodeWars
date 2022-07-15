def points(games):

    x = []

    for result in games:

        if int(result[0]) > int(result[2]):

            x.append(3)

        elif int(result[0]) < int(result[2]):

            x.append(0)

        elif int(result[0]) == int(result[2]):

            x.append(1)

    return sum(x)


print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))
# 30

print(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']))
# 10

print(points(['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4']))
# 0
