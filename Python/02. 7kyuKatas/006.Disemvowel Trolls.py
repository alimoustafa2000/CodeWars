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
