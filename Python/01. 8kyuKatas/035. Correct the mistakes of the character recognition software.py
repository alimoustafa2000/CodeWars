def correct(string):

    x = []

    for letter in string:

        if letter == '0':

            x.append('O')

        elif letter == '1':

            x.append('I')

        elif letter == '5':

            x.append('S')

        else:

            x.append(letter)

    result = "".join(x)

    return result

print(correct("L0ND0N"))
# LONDON

print(correct("51NGAP0RE"))
# SINGAPORE