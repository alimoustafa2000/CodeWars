# DESCRIPTION:
# Implement a function which convert the given boolean value into its string representation.

# Note: Only valid inputs will be given.

# ============
# Solution:
# ============

def boolean_to_string(b):

    if b == True:

        return "True"

    elif b == False:

        return "False"


print(boolean_to_string(True))
# True

print(boolean_to_string(False))
# False