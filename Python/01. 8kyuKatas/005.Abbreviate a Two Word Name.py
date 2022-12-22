# DESCRIPTION:
# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.

# It should look like this:
# Sam Harris => S.H
# patrick feeney => P.F

# ============
# Solution:
# ============

def abbrevName(name):
    first, last = name.upper().split(' ')
    return f"{first[0]}.{last[0]}"

print(abbrevName('Ali Moustafa'))
# A.M