import string

alphabet = set(string.ascii_lowercase)

def is_pangram(s):

    if set(s.lower()) >= alphabet :

        return True

    else:

        return False


print(is_pangram("The quick brown fox jumps over the lazy dog"))
# True

print(is_pangram("abcdfghijklmnopqrstuvxywz"))
# False
