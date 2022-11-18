def sort_array(source_array):

    x = []
    result = []

    for num in source_array:

        if num % 2 >= 1:

            x.append(num)

        else:

            pass


    x.sort()

    n = 0


    for number in source_array:

        if number % 2 >= 1:

            number = x[n]

            n += 1

            result.append(number)

        else:

            result.append(number)


    return(result)




print((sort_array([5, 3, 2, 8, 1, 4])))
# [1, 3, 2, 8, 5, 4]