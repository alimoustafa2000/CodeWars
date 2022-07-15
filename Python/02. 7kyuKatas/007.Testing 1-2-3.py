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
