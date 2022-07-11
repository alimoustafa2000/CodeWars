def no_space(x):

    a = []

    for letter in x:

        if letter == " ":

            continue

        else:

            a.append(letter)

    return "".join(a)



print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))
# 8j8mBliB8gimjB8B8jlB
