# DESCRIPTION:
# Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.
# When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.

# Your task is correct the errors in the digitised text. You only have to handle the following mistakes:
# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1

# The test cases contain numbers only by mistake.

# ============
# Solution:
# ============

def correct(string):

    x = []

    for letter in string:

        if letter == '0':

            x.append('O')

        elif letter == '1':

            x.append('I')

        elif letter == '5':

            x.append('S')

        else:

            x.append(letter)

    result = "".join(x)

    return result

print(correct("L0ND0N"))
# LONDON

print(correct("51NGAP0RE"))
# SINGAPORE