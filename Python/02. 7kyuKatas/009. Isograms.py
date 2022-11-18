def is_isogram(string):

    str = string.lower()

    x = []

    for let in str:

        x.append(let)

    for letter in x:

        n = x.count(letter)

        if n > 1:

            return False

        else:

            pass

    return True

print(is_isogram("Dermatoglyphics"))
# True

print(is_isogram("isIsogram"))
# False