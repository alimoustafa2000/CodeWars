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
