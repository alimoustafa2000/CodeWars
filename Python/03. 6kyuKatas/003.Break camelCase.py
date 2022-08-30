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
