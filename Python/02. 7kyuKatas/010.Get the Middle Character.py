# You are going to be given a word.
# Your job is to return the middle character of the word.
# If the word's length is odd, return the middle character.
# If the word's length is even, return the middle 2 characters.


def get_middle(s):

    x = len(s)

    if x % 2 == 0:

        z = int(x / 2)

        return f"{s[z - 1]}{s[z]}"

    elif x % 2 >= 1:

        y = int(x // 2)

        return s[y]


print(get_middle("test"))
# es

print(get_middle("testing"))
# t