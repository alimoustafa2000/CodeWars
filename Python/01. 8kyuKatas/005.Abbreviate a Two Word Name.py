def abbrevName(name):
    first, last = name.upper().split(' ')
    return f"{first[0]}.{last[0]}"

print(abbrevName('Ali Moustafa'))
# A.M