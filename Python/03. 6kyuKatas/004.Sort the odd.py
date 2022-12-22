# DESCRIPTION:
# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

# ============
# Solution:
# ============

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