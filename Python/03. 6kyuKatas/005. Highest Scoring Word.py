def high(x):

    my_list = x.split(" ")

    storage = []

    for item in my_list:

        n = []

        for letter in item:

            n.append(ord(letter) - 96)

        storage.append(sum(n))

        my_index = storage.index(max(storage))

    return my_list[my_index]



print((high('man i need a taxi up to ubud')))
# taxi