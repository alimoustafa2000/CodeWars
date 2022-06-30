def greet(name, owner):

    if name == owner:

        return "Hello boss"

    else:

        return "Hello guest"


print(greet('Daniel', 'Daniel'))
# Hello boss

print(greet('Greg', 'Daniel'))
# Hello guest