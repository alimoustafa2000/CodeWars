# DESCRIPTION:
# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.

# ============
# Solution:
# ============

def get_count(sentence):

    vowels = ['a', 'e', 'i', 'o', 'u']

    result = []

    for letter in sentence:

        if letter.lower() in vowels:

            result.append(letter)

    return len(result)


print(get_count("aeiou"))
# 5

print(get_count("bcdfghjklmnpqrstvwxz y"))
# 0
