# DESCRIPTION:
# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)
# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)
# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false

# ============
# Solution:
# ============

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