# DESCRIPTION:
# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

# ============
# Solution:
# ============

def bool_to_word(boolean):

    if boolean == True:

        return "Yes"

    elif boolean == False:

        return "No"


print(bool_to_word(True))
# Yes

print(bool_to_word(False))
# No