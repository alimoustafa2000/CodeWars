# DESCRIPTION:
# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
# Write a function which takes a list of strings and returns each line prepended by the correct number.
# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# Examples: (Input --> Output)
# [] --> []
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]

# ============
# Solution:
# ============

def number(lines):

    lines_with_counter = enumerate(lines, 1)

    final_result = []

    for counter, line in lines_with_counter:

        final_result.append((f"{counter}: {line}"))

    return final_result


print(number([]))
# []

print(number(["a", "b", "c"]))
# ['1: a', '2: b', '3: c']
