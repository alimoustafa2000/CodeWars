# DESCRIPTION:
# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

# ============
# Solution:
# ============

def even_or_odd(number):

    x = number % 2

    if x == 0:

        return "Even"

    else:

        return "Odd"

print(even_or_odd(10))
#Even

print(even_or_odd(15))
#Odd
