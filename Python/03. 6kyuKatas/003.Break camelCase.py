# DESCRIPTION:
# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

# ============
# Solution:
# ============

def solution(s):

    x = []

    for letter in s:

        if letter == letter.upper():

            n = letter.rjust(2,' ')

            x.append(n)

        else:

            x.append(letter)

    return "".join(x)


print(solution('helloWorld'))
# hello World
