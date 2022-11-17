def double_char(string):

    x = []

    for letter in string:

        x.append(letter * 2)

    result = "".join(x)

    return result

print(double_char("Hello World"))
# HHeelllloo  WWoorrlldd