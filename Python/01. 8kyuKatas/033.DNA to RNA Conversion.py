def dna_to_rna(dna):

    x = []

    for letter in dna:

        if letter == "T":

            x.append("U")

        else:

            x.append(letter)

    return "".join(x)


print(dna_to_rna("TTTT"))
# UUUU

print(dna_to_rna("GCAT"))
# GCAU
