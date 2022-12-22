# DESCRIPTION:
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

# ============
# Solution:
# ============

def double_char(string):

    x = []

    for letter in string:

        x.append(letter * 2)

    result = "".join(x)

    return result

print(double_char("Hello World"))
# HHeelllloo  WWoorrlldd