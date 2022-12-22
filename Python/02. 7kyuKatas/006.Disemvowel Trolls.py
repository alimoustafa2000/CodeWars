# DESCRIPTION:
# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example: 
# The string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.

# ============
# Solution:
# ============

def disemvowel(string_):

    vowels = ['a', 'e', 'i', 'o', 'u']

    result = []

    for letter in string_:

        if letter.lower() in vowels:

            continue

        else:

            result.append(letter)

    final_result = "".join(result)

    return final_result


print(disemvowel("This website is for losers LOL!"))
# Ths wbst s fr lsrs LL!
